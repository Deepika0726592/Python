#!/usr/bin/python

import gitlab
import sys
import argparse

def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='creating new branch')
    parser.add_argument('--current-branch', help='current branch', required=True)
    parser.add_argument('--release-branch', help='release branch', required=True)
    args = parser.parse_args()
    return args


def create_branch(args):
    """
    Creating new branch in git
    """ 
    gl = gitlab.Gitlab.from_config('gitlab', ['/home/user/.python-gitlab.cfg'])
    group = gl.groups.get('5')
    for project in group.projects.list(all=True):
        project = gl.projects.get(project.id)
        branch = project.branches.get(args.current_branch)
        if branch:
            print('current branch exists in this repo, hence creating a new branch')
    #        branch = project.branches.create({'branch': 'args.release_branch',
    #                                  'ref': 'master'})

def main():
    """
    Main entry into the script
    """
    args = parse_args()
    create_branch(args)


if __name__ == '__main__':
     main()
