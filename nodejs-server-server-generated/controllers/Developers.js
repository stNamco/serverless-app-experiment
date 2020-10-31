'use strict';

var utils = require('../utils/writer.js');
var Developers = require('../service/DevelopersService');

module.exports.createUser = function createUser (req, res, next) {
  Developers.createUser()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.createUserAndPokemonRelationship = function createUserAndPokemonRelationship (req, res, next, userId, pokemonId) {
  Developers.createUserAndPokemonRelationship(userId, pokemonId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getAllPokemon = function getAllPokemon (req, res, next, offset, limit) {
  Developers.getAllPokemon(offset, limit)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getAllUsers = function getAllUsers (req, res, next) {
  Developers.getAllUsers()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getPokemon = function getPokemon (req, res, next, pokemonId) {
  Developers.getPokemon(pokemonId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getUser = function getUser (req, res, next, userId) {
  Developers.getUser(userId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getUserAndPokemonRelationship = function getUserAndPokemonRelationship (req, res, next, userId, pokemonId) {
  Developers.getUserAndPokemonRelationship(userId, pokemonId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
