# AirBnB_clone
Building my first full web application: the Airbnb clone

## Table of contents
- [Project Description](#project-Description)
  - [Overview](#project-overview)
  - [Project Implementation Steps](#projects-steps)
      - [The Console](#the-console)
- [Command Interpreter Description](#console-Description)

## Project Description
The AirBnB clone project lasts until… four months from now. The project aims to deploy a simple copy of the [AirBnB website](https://www.airbnb.com/) on my server.

### Project Overview

After 4 months, I will have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front end and my data (retrieve, create, delete, update them)

### Project Steps

#### Project Steps

**First step: Write a command interpreter to manage your AirBnB objects.**

This is the first step towards building my first full web application: the AirBnB clone. This first step is very important because I will use what I build during this project with all other following projects: `HTML/CSS templating`, `database storage`, `API`, `front-end integration`…

Each task is linked and will help to:

- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization, and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## Console Description
