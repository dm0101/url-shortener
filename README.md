# url-shortener<br />
Demo django rest framework project for url shortner<br />
<br />
What it does.<br />
1.Take a long url and give short URL<br />
2.Shortened URl five count fo total hits and hits in last one hour.<br />
3.Search URL based on partial or exact match in long URL title.<br />
<br />
Steps to run:<br />
1.Install Python 3+<br />
2.Install Virtualenv using pip<br />
3.Create virtualenv using command "virtualenv project_name"<br />
4.Git clone the project<br />
5.Go to url_shortener folder<br />
6.Run command "pip install -r requirements.txt"<br />
7.Start django server using command "python manage.py runserver"<br />
<br />
How to test the URL:<br />
Since the project was to make API to create short URL,I have make REST API for the same.The prefered way to test the API will be using POSTMAN for the same.<br />
<br />
1.Take a long url and give short URL<br />
API END- http://127.0.0.1:8000/short/<br />
Method - POST<br />
Data body to be sent - {<br />
	"full_url":"http://www.example.com"<br />
}<br />
<br />
2.Shortened URl five count fo total hits and hits in last one hour.<br />
API END- <returned short url from step one><br />
Method - GET<br />
<br /><br />
3.Search URL based on partial or exact match in long URL title.<br />
API END- http://127.0.0.1:8000/search/<br />
Method - POST<br />
Data body to be sent - {<br />
	"search_term":"search word from the long url"<br />
}<br />
<br />
4.Get list of all short URL<br />
API END- http://127.0.0.1:8000/short/<br />
Method - GET<br />
<br />
Alternatively,the API can be tested using Browser also.<br />
