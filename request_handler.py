from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs
from views import (
    get_all_comments,
    get_single_comment,
    get_all_posts,
    get_single_post,
    update_comment,
    delete_comment,
    create_post,
    update_post,
    delete_post,
    get_single_sub,
    get_all_subs,
    create_sub,
    update_sub,
    delete_sub,
    get_comments_by_post,
    get_subscribed_posts,
    get_all_tags,
    update_tag,
    create_tag,
    delete_tag,
    get_all_post_tags,
    create_post_tag,
    remove_post_tag,
    get_all_categories,
    get_single_category,
    create_category,
    update_category,
    delete_category,
    create_comment,
    )
from views.reaction_requests import get_all_reactions


from views.user import create_user, login_user
class HandleRequests(BaseHTTPRequestHandler):

    # def parse_url(self, path):
    #     """Parse the url into the resource and id"""
    #     path_params = self.path.split('/')
    #     resource = path_params[1]
    #     if '?' in resource:
    #         param = resource.split('?')[1]
    #         resource = resource.split('?')[0]
    #         pair = param.split('=')
    #         key = pair[0]
    #         value = pair[1]
    #         return (resource, key, value)
    #     else:
    #         id = None
    #         try:
    #             id = int(path_params[2])
    #         except (IndexError, ValueError):
    #             pass
    #         return (resource, id)

    # replace the parse_url function in the class
    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        self._set_headers(200)
        response = {}

        parsed = self.parse_url(self.path)

        if '?' not in self.path:
            ( resource, id ) = parsed

            if resource == "posts":
                if id is not None:
                    response = f"{get_single_post(id)}"
                else:
                    response = f"{get_all_posts()}"
            if resource == "comments":
                if id is not None:
                    response = f"{get_single_comment(id)}"
                else:
                    response = f"{get_all_comments()}"
            if resource == "subscriptions":
                if id is not None:
                    response = f"{get_single_sub(id)}"
                else:
                    response = f"{get_all_subs()}"
            if resource == "categories":
                if id is not None:
                    response = f"{get_single_category(id)}"
                else:
                    response = f"{get_all_categories()}"
            if resource == "tags":
                if id is not None:
                    pass
                else:
                    response = f"{get_all_tags()}"
            if resource == "posttags":
                if id is not None:
                    pass
                else:
                    response = f"{get_all_post_tags()}"
            if resource == "reactions":
                if id is not None:
                    pass
                else:
                    response = f"{get_all_reactions()}"
        else: #there is a ? in the path.
            (resource, query) = parsed
            if query.get('user_id') and resource == 'posts':
                response = get_subscribed_posts(query['user_id'][0])

            if query.get('post_id') and resource == 'comments':
                response = get_comments_by_post(query['post_id'][0])

        self.wfile.write(response.encode())


    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        resource, _ = self.parse_url(self.path)

        new_post = None
        new_sub = None
        new_tag = None
        new_post_tag = None
        new_comment = None

        if resource == 'login':
            response = login_user(post_body)
        if resource == 'register':
            response = create_user(post_body)
        if resource == "posts":
            new_post = create_post(post_body)
            self.wfile.write(f"{new_post}".encode())
        if resource == "subscriptions":
            new_sub = create_sub(post_body)
            self.wfile.write(f"{new_sub}".encode())
        if resource == "categories":
            new_post = create_category(post_body)
            self.wfile.write(f"{new_post}".encode)
        if resource == "tags":
            new_tag = create_tag(post_body)
            self.wfile.write(f"{new_tag}".encode())
        if resource == "posttags":
            new_post_tag = create_post_tag(post_body)
            self.wfile.write(f"{new_post_tag}".encode())
        if resource == "comments":
            new_comment = create_comment(post_body)
            self.wfile.write(f"{new_comment}".encode())

        self.wfile.write(response.encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "comments":
            success = update_comment(id, post_body)
        elif resource == "posts":
            success = update_post(id,post_body)
        elif resource == "subscriptions":
            success = update_sub(id, post_body)
        elif resource == "tags":
            success = update_tag(id, post_body)
        elif resource == "categories":
            success = update_category(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)
        self.wfile.write("".encode())

    def do_DELETE(self):
        """Handle DELETE Requests"""
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        if resource == "comments":
            delete_comment(id)
        elif resource == "posts":
            delete_post(id)
        elif resource == "subscriptions":
            delete_sub(id)
        elif resource == "tags":
            delete_tag(id)
        elif resource == "posttags":
            remove_post_tag(id)
        elif resource == "categories":
            delete_category(id)

        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
