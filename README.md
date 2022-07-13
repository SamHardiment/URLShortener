# LAP 4 CODE CHALLENGE

The Challenge: To build a URL shortener for web urls
The Team: [Sam](https://github.com/SamHardiment) and [Amir](https://github.com/aha000111)

Example:

1. Type `gg` in to the searchbar
2. You should be redirected to www.google.com

### Installation

- Clone repo and cd into the folder
- Install pipenv if not already installed
- Run `pipenv install` to install dependencies

### Usage

If you decide to run server locally, you will have to change the links in the home() route to your localhost:5000 address.

- Run `pipenv run dev` to launch server locally.

Otherwise visit our app launched on an heroku server at:

[https://url-but-short.herokuapp.com/](https://url-but-short.herokuapp.com/)

## Area's of difficulty

We are struggling to use the searchbar on the new redirected route and we believe it is due to the new route we are located on which doesn't have the route home() POST functionality.
