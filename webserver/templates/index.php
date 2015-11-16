<!DOCTYPE html>
<html>

<head>
    <title>Brown Sports</title>
    <link href='https://fonts.googleapis.com/css?family=Raleway:300' rel='stylesheet' type='text/css'>  
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="{{url_for('static', filename='main.css')}}">
</head>

<body>  
    <div id="wrapper">
        <div id="header">
            <a href="#">
                <img class="center-block" src="http://i.imgur.com/hfhRSSJ.jpg" height="100">
            </a>
        </div>
    </div>
    <div id="content">
        <div class="jumbotron"> 
            <div class="greetings"> 
                <h2>
                    ask us about any current team or player from the nfl or nba
                </h2>   
                <div class="col-sm-8 col-md-7 col-md-offset-5" style="min-width: 500px;" id="searchdiv">
                    <form method="post" action=search.php?go></form>
                        <input type="text" name="name" placeholder="Ex: Kobe Bryant...Lakers...">
                        <input type="submit" value="Search" name="submit" class="btn btn-default">
                    </form>
                </div>
            </div>  
        </div>
    </div>
    <div id="footer">
    </div>
</body>


