import requests

class Response:
    def __init__(self, r=None):
        self.r = r

    @staticmethod
    def parse(data):
        if isinstance(data, dict):
            parsed_data = Response()
            for key, value in data.items():
                setattr(parsed_data, key, Response.parse(value))
            return parsed_data
        elif isinstance(data, list):
            parsed_data = []
            for item in data:
                parsed_item = Response.parse(item)
                parsed_data.append(parsed_item)
            return parsed_data
        else:
            return data
            
    def traverse(self, print_fn, depth=0):
        attr_names = [attr for attr in dir(self) if not attr.startswith('__') and not callable(getattr(self, attr)) and attr != 'r']
        for attr in attr_names:
            value = getattr(self, attr)
            if isinstance(value, Response):
                print_fn(f"{'  '*depth}{attr}:")
                value.traverse(print_fn, depth+1)
            elif isinstance(value, list) and all(isinstance(v, Response) for v in value):
                print_fn(f"{'  '*depth}{attr} (list):")
                for v in value:
                    v.traverse(print_fn, depth+1)
            else:
                print_fn(f"{'  '*depth}{attr}: {value}")

