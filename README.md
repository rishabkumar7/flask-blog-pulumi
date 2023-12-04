# Flask Blog App with DynamoDB

This project is a simple blog application built with Flask, a micro web framework written in Python. The application uses Amazon DynamoDB as its backend database, demonstrating the integration of a Flask application with AWS services.

## Features

- Create, view, and list blog posts
- Backend storage with AWS DynamoDB
- Simple UI using Bootstrap

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.8 or later
- Flask
- Boto3 (AWS SDK for Python)
- AWS account and credentials

### Installing

A step-by-step series of examples that tell you how to get a development environment running:

1. **Clone the repository**

   ```bash
   git clone https://github.com/rishabkumar7/flask-blog-pulumi.git
   cd your-repo-name
   ```

2. **Set up a virtual environment (optional but recommended)**:

  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```

3. **Install required packages:**

  ```bash
  pip install -r requirements.txt
  ```

4. **Set up AWS Credentials:**

Ensure your AWS credentials are set up correctly in your environment.
Look at the `.env.example`

5. **Run the application:**

  ``` bash
  flask run
  ```

Your app should now be running on http://localhost:5000.

## Configuration

AWS DynamoDB Table: Make sure to create a DynamoDB table with the required schema.

Primary Key:
`post_id` (String) - A unique identifier for each blog post, usually a UUID.

Attributes:

- post_id (String) - Unique identifier for the post.
- title (String) - The title of the blog post.
- content (String) - The main content/body of the blog post.
- author (String) - The author's name or identifier.
- date (String or Number) - The date the post was created or published. This could be a string in ISO format or a Unix timestamp.
- tags (List of Strings) - Tags or categories associated with the post.

``` json
{
  "post_id": "123e4567-e89b-12d3-a456-426614174000",
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post...",
  "author": "Jane Doe",
  "date": "2023-03-01T12:00:00Z",
  "tags": ["Cloud", "AWS"],
  "status": "published"
}
```

## Usage

The application is straightforward to use. Navigate to the home page to view a list of blog posts. Use the 'Create New Post' button to add a new blog post.

## Contributing

Please read `CONTRIBUTING.md`` for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

Rishab Kumar - @rishabkumar7

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
