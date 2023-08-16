# evidentbdtest

Run `python.exe main.py` in the root directory of the repo to run the code.

## Framework- Flask
## Database- MySQL

##API Endpoint call manual:
{
Open Postman and create a new request:

Click on the "New" button in the upper left corner.
Select "Request."
Set Up the Request:

In the request configuration panel, give your request a name (e.g., "Get Input Values").
Choose the HTTP method as "GET".
Enter the URL for your API endpoint. For example: http://localhost:5000/api/get_input_values.
Add Query Parameters:
Since your API endpoint requires query parameters (start_datetime, end_datetime, user_id), you need to include them:

Click on the "Params" button below the URL input field.
Add the query parameters:
Key: start_datetime, Value: 2023-01-01 00:00:00 (an appropriate date and time)
Key: end_datetime, Value: 2023-08-31 23:59:59 (an appropriate date and time)
Key: user_id, Value: 1 (replace with an appropriate user ID)
Send the Request:

Click the "Send" button to send the request to your API endpoint.
View Response:

Postman will show the response received from your API endpoint in the lower part of the screen. The response should match the format you defined.
}
##Sample Query :- `http://localhost:5000/api/get_input_values?start_datetime=2023-08-16 22:42:37&end_datetime=2023-08-16 22:55:48&user_id=1`
