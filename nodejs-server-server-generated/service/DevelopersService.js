'use strict';


/**
 * create a new user
 * create a new user
 *
 * returns User
 **/
exports.createUser = function() {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "name" : "yojan",
  "userId" : "123e4567-e89b-12d3-a456-426614174000"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * create a relationship between a user and a pokemon
 * create a relationship between a user and a pokemon
 *
 * userId String user id
 * pokemonId Integer pokemon id
 * returns UserPokemonDetail
 **/
exports.createUserAndPokemonRelationship = function(userId,pokemonId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "createdAt" : "20/10/2020",
  "pokemonId" : 1,
  "userAndPokemonRelationshipId" : "123e4567-e89b-12d3-a4f6-42661417e000",
  "userId" : "123e4567-e89b-12d3-a456-426614174000"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * get a list of all pokemons paginated 20 by 20
 * Get all pokemons paginated 20 by 20 only calling this path with or without arguments 
 *
 * offset Integer Number where pagination starts (optional)
 * limit Integer number of records to skip for pagination (optional)
 * returns List
 **/
exports.getAllPokemon = function(offset,limit) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "pokemonId" : 1,
  "name" : "bulbasaur",
  "url" : "https://pokeapi.co/api/v2/pokemon/1/"
}, {
  "pokemonId" : 1,
  "name" : "bulbasaur",
  "url" : "https://pokeapi.co/api/v2/pokemon/1/"
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * get a list of registered users
 * get all users with basic information
 *
 * returns List
 **/
exports.getAllUsers = function() {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "name" : "yojan",
  "userId" : "123e4567-e89b-12d3-a456-426614174000"
}, {
  "name" : "yojan",
  "userId" : "123e4567-e89b-12d3-a456-426614174000"
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * get a specific pokemon by id
 * get a pokemon using their unique id
 *
 * pokemonId Integer it's the pokemon id
 * returns Pokemon
 **/
exports.getPokemon = function(pokemonId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "pokemonId" : 1,
  "name" : "bulbasaur",
  "url" : "https://pokeapi.co/api/v2/pokemon/1/"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * get an user with their pokemons
 * get an specific user with their catched pokemons
 *
 * userId String it's the user id
 * returns UserDetail
 **/
exports.getUser = function(userId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "pokemons" : [ {
    "pokemonId" : 1,
    "name" : "bulbasaur",
    "url" : "https://pokeapi.co/api/v2/pokemon/1/"
  }, {
    "pokemonId" : 1,
    "name" : "bulbasaur",
    "url" : "https://pokeapi.co/api/v2/pokemon/1/"
  } ],
  "name" : "yojan",
  "userId" : "123e4567-e89b-12d3-a456-426614174000"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * get a relationship between an user and a pokemon
 * get all information related in the relationship between a pokemon and a user
 *
 * userId String user id
 * pokemonId Integer pokemon id
 * returns UserPokemonDetail
 **/
exports.getUserAndPokemonRelationship = function(userId,pokemonId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "createdAt" : "20/10/2020",
  "pokemonId" : 1,
  "userAndPokemonRelationshipId" : "123e4567-e89b-12d3-a4f6-42661417e000",
  "userId" : "123e4567-e89b-12d3-a456-426614174000"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}

