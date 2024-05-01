## Flask Application Design

### HTML Files

- **index.html**: This file will serve as the main page for the application. It will include the necessary HTML elements for the entry box, submit button, and display area for previous queries.

### Routes

- **@app.route('/'):** This route will handle GET requests for the main page. It will render the index.html file.
- **@app.route('/submit_query', methods=['POST']):** This route will handle POST requests sent when the user submits a query. It will extract the query from the request, call the vertexai/gemini API to get a response, and store the query and response in a database or other persistent storage. It will then redirect the user back to the main page.