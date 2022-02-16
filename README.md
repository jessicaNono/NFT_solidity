# NFT 

The objective of this project is to tokenise a land title. 

We will use the erc-721 standard to create an NFT of a signed digital document (.pdf).
Documentation (fr): https://jessicanono.filparty.com/nft-sur-ethereum

## Disclaimer

**Kindly read the code of conduct https://github.com/jessicaNono/NFT_solidity/blob/main/CODE_OF_CONDUCT.md**

## How to start

   ### clone the repositery 
     ```
     // open your terminal 
     cd desktop
     git clone https://github.com/jessicaNono/NFT_solidity
     // go to the cloned project
     cd NFT_solidity
     ```
     
 ## Installation
 
  - [Truffle](https://trufflesuite.com/docs/truffle/quickstart.html) A world class development environment, testing framework and asset pipeline for blockchains using the Ethereum Virtual Machine (EVM), aiming to make life as a developer easier. 
 
  - [ganache](https://trufflesuite.com/docs/ganache/) a personal blockchain for rapid Ethereum and Corda distributed application development. You can use Ganache across the entire development cycle; enabling you to develop, deploy, and test your dApps in a safe and deterministic environment.
 
  - [open zeppelin](https://openzeppelin.com/) The standard for secure blockchain applications
OpenZeppelin provides security products to build, automate, and operate decentralized applications. We also protect leading organizations by performing security audits on their systems and products.
 
 
 ## Deploiement
  
   ### Deploy "LTL" to the network filparty(https://github.com/filparty/filparty_network)

* Using truffle: truffle migrate --network filparty
* see truffle-config.js
