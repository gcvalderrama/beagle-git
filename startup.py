from git import Repo
from datetime import datetime

if __name__ == '__main__':
    

# url = 'https://github.com/username/repo.git'  # URL of the git repository
# path_to_clone_to = '/path/to/local/directory'  # Path to the local directory where the repo will be cloned

# # Clone the repository
# Repo.clone_from(url, path_to_clone_to)
    repo = Repo('C:/github/vscode')  # Path to your local git repository
    origin = repo.remotes.origin
    # Print all commit messages for all branches
    # for ref in repo.remotes.origin.refs:
    #     print(ref.name)
    #     print(ref.remote_head)
    #     print(ref.remote_name)
    #     repo.git.checkout(ref.remote_head)                
    #     repo.git.reset('--hard', 'HEAD~1')
        

        # for commit in repo.iter_commits(ref.remote_head):
        #     print(f'Commit in {ref.remote_head}: {commit.message}')
        #     break
    # for ref in repo.remotes.origin.refs:        
    #     name = ref.name.replace("origin/","")
    #     print(ref.name)
    #     print(name)
    #     repo.git.checkout(name)        
        
        
    count = 0
    # for branch in repo.branches:
    #     print(branch.name)
    for commit in repo.iter_commits():
        print(commit.hexsha)
        print(commit.author.email)
        print( datetime.fromtimestamp( commit.authored_date))        
        print(commit.message)
        print(commit.stats)
        for file in commit.stats.files:
            d = commit.stats.files[file]
            print(file)            
        if count == 2:
            break
        count += 1
