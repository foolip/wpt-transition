import os

from github import Github, GithubException


def main():
    token = os.environ['GH_TOKEN']
    g = Github(token)
    w3c_org = g.get_organization('w3c')
    wpt_org = g.get_organization('web-platform-tests')
    wpt_repo = w3c_org.get_repo('web-platform-tests')

    teams = wpt_org.get_teams()
    reviewers = next(t for t in teams if t.name == 'reviewers')

    # this includes collaborators via teams
    all_users = set(wpt_repo.get_collaborators())

    for user in sorted(all_users, key=lambda user: user.login):
        if user.permissions.push:
            print(user.login, 'has write access, adding to reviewers')
            try:
                reviewers.add_to_members(user)
            except GithubException as e:
                print(user.login, e)

if __name__ == '__main__':
    main()
