import os
import sys

from github import Github, GithubException


def main():
    token = os.environ['GH_TOKEN']
    g = Github(token)
    wpt_org = g.get_organization('web-platform-tests')

    teams = wpt_org.get_teams()
    reviewers = next(t for t in teams if t.name == 'reviewers')

    logins = set(user.login for user in reviewers.get_members())

    for login in sys.stdin.read().split():
        if login.startswith('@'):
            login = login[1:]
        if login in logins:
            #print(login, 'already in the reviewers team')
            continue
        try:
            reviewers.add_to_members(g.get_user(login))
            print(login, 'added to the reviewers team')
            logins.add(login)
        except GithubException as e:
            print(login, e)

if __name__ == '__main__':
    main()
