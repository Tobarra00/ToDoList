<header>
    <h1>To Do List 📝</h1>
</header>

<div>
    <p>This project focuses in CRUD operations. With this application, you are able to create, search, edit and delete a task. It also supports user registration and authentication, so that a user can only see his tasks and not other's. 
    </p>
    <p>Here are some spoilers on what you can expect:</p>
    <br><br>
    <img src="images/Tasks.png" alt="Project directory" width="350"> &emsp;&emsp;&emsp;
    <img src="images/Login.png" alt="Project directory" width="350" height='188'>
    <br><br>
    
</div>

<section>
    <h2>Technologies 🧑‍💻</h2>
    <p>These are the technologies used in this project:</p>
    <ul>
        <li>Python</li>
        <li>Django</li>
        <li>SQLite3</li>
        <li>HTML</li>
        <li>CSS</li>
    </ul>

</section>

<section>
    <h2>How to make it work 🔧</h2>
    <p>In this section I will show step by step how to make this code work:</p>
    <ol>
        <li>Use <code>git clone</code> to clone the repository or download the <code>ToDoList</code> directory. After that, open an editor and navigate to the project directory where the <code>ToDoList</code> directory is. Then create a virtual environment with:<br><br>
        <ul>
            <li><code>pip install virtualenv</code><br><br></li>
            <li><code>virtualenv venv</code><br><br></li>
        </ul>
        After that, activate the virtual environment and use this command to install the requirements to make the project work properly:<br><br>
        <ul>
            <li><code>pip install -r requirements.txt</code><br><br></li>
        </ul>
        It should look something like this:
        <br><br>
        <img src="images/Project directory.png" alt="Project directory" width="350">
        <br><br>
        </li>
        <li>The next step is to manage the database. To create a <code>sqlite3</code> database, execute these commands before running the server:<br><br>
            <ul>
                <li><code>python manage.py makemigrations</code><br><br></li>
                <li><code>python manage.py migrate</code><br><br></li>
            </ul>
        </li>
        <li>To wrap things up, go to the <code>ToDoList/ToDoList</code> directory and open the <code>.env.txt</code> file. Here you have to replace the asigned values of the variables with your own data. For example:<br><br>
            <ul>
                <li>
                    In <code>SECRET_KEY=your_secret_key</code>, replace <code>your_secret_key</code> with your secret key, which you can generate by your own or use:<br>
                    <code>from django.core.management.utils import get_random_secret_key</code>.<br><br>
                </li>
                <li>
                    In <code>DEBUG=true_or_false</code>, replace <code>true_or_false</code> with the <code>True</code> or <code>False</code>, depending on what you want to do.<br><br>
                </li>
                <li>
                    In <code>TEMPLATES_DIR=templates_directory</code>, replace <code>templates_directory</code> with the path to the directory where you store your django templates.<br><br>
                </li>
                <li>
                    In <code>STATIC=static</code>, replace <code>static</code> with the path to the directory with the static files.<br><br>
                </li>
            </ul>
        ⚠️ To make these variables work, just <strong>delete</strong> the <code>.txt</code> extension of the file.<br><br>
        </li>  
        <li>Finally, if everything went right, you should be able to run the server and visualize the website and utilize its functionalities by using the command:<br><br>
            <ul>
                <li><code>python manage.py runserver</code><br><br></li>
            </ul>
        </li>
        <li>And that's all, you should be able to navigate and try the website with all of its functionallity 😉.<br><br></li>
    </ol>
</section>

<section>
    <h2>
        Contact me:
    </h2>
    <p>In case you have any doubt or you are interested about my work, you can contact me here: </p>
    <ul>
        <li>My linkedin: <a href="https://www.linkedin.com/in/pedro-tobarra-leal/"><img src="images/linkedin.png" alt="linkedin" width="20"></a></li>
        <li>My email: <a href="mailto:pedro.tobarra.leal@gmail.com">Pedro.tobarra.leal@gmail.com</a></li>
    </ul>
</section>
