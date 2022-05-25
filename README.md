# Dathomir

Python project to clone all `gitlab` or `github` repositories using gitlab api

**_Version: 1.0.0_**

## Summary

- [Requirements](#requirements)
- [Get started](#get-started)
- [How it works](#how-it-works)
- [How to use](#how-to-use)
  - [GitHub Account](#on-github-account)
  - [GitLab Account](#on-gitlab-account)
  - [Self-host Gitlab](#on-self-host-gitlab-instance)
- [Options](#options)
- [Unit tests](#tests)
- [VS Code](#vs-code)
- [Formatting](#formatting)
- [Contact](#formatting)
- [Credits](#credits)

## Requirements

- [Python](https://www.python.org/) >= 3.9.5

packages to install with pip

```bash
python3 -m pip install --user pip install virtualenv
python3 -m pip install --user pip install pep8
```

## Get started

If you don't have python

```bash
$ [sudo] apt-get install python3
$ pip install virtualenv
```

```bash
$ git clone git@github.com:LucasNoga/dathomir.git
$ cd dathomir
$ virtualenv -p 3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ cp config.example.json config.json
$ python3 .
```

## How it works

The script connect to a git server account (Gitlab or Github) and use the REST API to get all repository of the account and clone it

These repositories go to `repositories folder`

## How to use

You have to setup your `config.json` file in `.` directory

After you need to setup your `Github` or `Gitlab` account

### On GitHub Account

- Go to your account via: `https://github.com/login`
- Your tooken ca be generate into: `https://github.com/settings/tokens`
- Select the scope `public_repo` or `repo` (get private repo)
- Click to generate token
- Copy-Paste the token just generated into `<GITHUB_TOKEN>`

```json
{
  "type": "github",
  "url": "https://github.com",
  "token": "<GITHUB_TOKEN>"
}
```

### On GitLab Account

- Go to your account via: `https://gitlab.com/users/sign_in`
- Your token ca be generate into: `https://gitlab.com/-/profile/personal_access_tokens`
- Select the scope `read-api` and `read-repository`
- Click to generate token
- Copy-Paste the token just generated into `<GITLAB_TOKEN>`

```json
{
  "type": "gitlab",
  "url": "https://gitlab.com",
  "token": "<GITLAB_TOKEN>"
}
```

### On Self-Host Gitlab instance

- Your url can be `your-company.gitlab.com`
- Your token can be generate into `https://your-company.gitlab.com/-/profile/personal_access_tokens`
- Select the scope `read-api` and `read-repository`
- Click to generate token
- Copy-Paste the token just generated into `<GITLAB_TOKEN>`

```json
{
  "type": "gitlab",
  "url": "https://your-company-gitlab.com",
  "token": "<GITLAB_TOKEN>"
}
```

Then launch the script `python . --console`  
and select the config you want to get a backup

All repositories will be store in `./repositories` folder

## Options

Launch config mode
You can directly modify `config.json` file through the app

```bash
$ python3 dathomir.py --config
```

in this mode you can

- Add new config server
- Remove config server already in config

Launch debug mode

```bash
$ python3 dathomir.py -d
$ python3 . -d
$ python3 dathomir.py --debug
$ python3 . --debug
```

Launch console app

```bash
$ python3 . -c
$ python3 . --console
```

## Tests

To execute all unit tests

```bash
$ python -m unittest discover
$ python -m unittest
```

To execute unit tests for module

```bash
$ python -m unittest helper
$ python -m unittest core
```

## VS Code

To add in `settings.json`

```js
  "python.linting.pylintArgs": [
    "--disable=W0703", // W0703: Generic Exception
    "--load-plugins",
    "pylint_flask_sqlalchemy",
    "pylint_flask"
  ]
```

## Formatting

The source code is format with the [pep8 guidelines](https://peps.python.org/pep-0008/)  
The source code is validating by [pylint](https://pylint.pycqa.org/en/latest/)

## Contact

- To make a pull request: https://github.com/LucasNoga/dathomir/pulls
- To summon an issue: https://github.com/LucasNoga/dathomir/issues
- For any specific demand by mail: [luc4snoga@gmail.com](mailto:luc4snoga@gmail.com?subject=[GitHub]%20Dathomir%20Project)

## Credits

Made by Lucas Noga.  
Licensed under GPLv3.
