helpers = {
    'Hello World': 'print(\'Hello, World!\')',
    'For Loop': 'for i in range(10):\n    print(i)',
    'Numpy Array': 'import numpy as np\n\narr = np.array([1, 2, 3])\nprint(arr)'
}

rest_api = {
    'Get Request': 'import requests\n\nresponse = requests.get(\'https://jsonplaceholder.typicode.com/todos/1\')\nprint(response.json())',
    'Post Request': 'import requests\n\npayload = {\'title\': \'foo\', \'body\': \'bar\', \'userId\': 1}\nresponse = requests.post(\'https://jsonplaceholder.typicode.com/posts\', json=payload)\nprint(response.json())',
    'Put Request': 'import requests\n\npayload = {\'title\': \'foo\', \'body\': \'bar\', \'userId\': 1}\nresponse = requests.put(\'https://jsonplaceholder.typicode.com/posts/1\', json=payload)\nprint(response.json())'
}