import os

from github import Github


def main():
    token = os.environ['GH_TOKEN']
    g = Github(token)
    w3c_org = g.get_organization('w3c')
    wpt_org = g.get_organization('web-platform-tests')
    wpt_repo = w3c_org.get_repo('web-platform-tests')

    invited_users = set(wpt_org.get_members())

    # this includes collaborators via teams
    all_users = set(wpt_repo.get_collaborators())

    for user in sorted(all_users, key=lambda user: user.login):
        if user in invited_users:
            print('Skipping {} (already invited)'.format(user.login))
            continue
        print('Inviting {}'.format(user.login))
        wpt_org.add_to_members(user, role='member')


if __name__ == '__main__':
    main()
