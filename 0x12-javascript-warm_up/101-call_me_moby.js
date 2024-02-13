#!/usr/bin/node


function callMeMoby(number, theFunction) {
    for (let x = 0; x < number; x++) {
        theFunction();
    }
}

module.exports.callMeMoby = callMeMoby;
