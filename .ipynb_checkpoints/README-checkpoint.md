# datafun-04-jupyter
Module 4 of 44608

1. I created the github with the name datafun-04-jupyter and added the file READ.ME
2. Created the folder in finder (datafun-04-jupyter) in the parent folder documents>NWMO
3. Copied the URL from github with the new repository name (datafun-04-jupyter)
4. I opened VS code and did open file and went to documents>NWMO>datafun-04-jupyter
5. Open new terminal and did: git clone datafun-04-jupyter
6. I created Create a Project Virtual Environment in VS code typed: python3 -m venv .venv
7. Activate Project Virtual Environment in VS typed: source .venv/bin/activate
8. in vs code, went to file>new file and created a requirements.txt
9. packages were installed: python3 -m pip install requests
10. requirements.txt was installed: pip install -r requirements.txt
11. freezed requirements: python3 -m pip freeze > requirements.txt
12. verified the following were installed in the folder in finder (making sure the hiding folder are showin)
venv/, .gitignore, README.md and requirements.txt
13. performed git add and commited initial changes with a message: 
git add .
git commit -m "initial commit"
14. performed gitpush to github: git push origin main
15. confirmed in github that the changes are showinf as "commit"

## How to Install and Run the Project ##

open native terminal in MacOs
navigate to project directory
`use cd command`
create virtual environment 
`use venv`
python3 -m venv venv
activate virtual environment: source venv/bin/activate
install packages
use `pip`
pip install `package_name`
freeze dependencies