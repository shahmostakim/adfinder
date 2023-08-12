For a given article or blog site, this web application finds relevant ads from the ads stored in database based on keyword analysis. Built with Django, Tailwind, RakeNLTK, BeautifulSoup

============ How to Run ============

    Install docker on your local machine
    Go to terminal and run "docker login". Use your docker login credentials.
    Run "docker pull shahmostakim/adfinder:withdata"
    Run "docker run -p 8555:8000 shahmostakim/adfinder:withdata"
    Open browser and visit "localhost:8555"


=========== Note ===================

    It is strongly recommended to run the project with docker image. Github repository is best for code review only. 
    
    you can change the host machine port number that maps to docker port number. Just replace '8555' with your desired port number in the "docker run" command.
    To create new ads and tags in database login with username: "shah", password: "dimuna2012".

    Project Demo: https://youtu.be/X0TJSoPTpiY

