var Epitech = artifacts.require("MyNFT");
  // Is there is an injected web3 instance?
module.exports = function(deployer) {
  deployer.deploy(Epitech);
};