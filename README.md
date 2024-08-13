Introduction: Install BTC and update to the latest block, use bitcoin-utxo-dump-master to obtain and parse all utxo, get all BTC accounts with balance and convert them to csv. 
Use qz.py to filter, get all accounts with balance above 0.7BTC and generate them into txt. 
Finally, use btckeygen-master to batch generate private keys and convert them to various addresses and check whether there is balance.

this project use go and python. the bitcoin-utxo-dump-master is quote.  

about btckeygen-master. Because the BTC collision is queried from memory. So the speed is very fast, about 8000 times per second. This is the result of multi-threading. If your PC configuration is better, you can modify the code to add more threads to increase the speed.

about example as the txt for p2pkh_1Aszdx.txt. all the p2pkh and The second character is a number and the last character is A-Z.
about example as the txt for p2pkh_Aaszdx.txt. all the p2pkh and The second character is a A-Z and the last character is a-z.

way 1:
  step 1. install btc, and update block to newest.
  step 2. download bitcoin-utxo-dump-master. change dir for the btc dir and output dir.
  step 3. download the qz.py. change dir for the btc-balance.csv dir and output dir.
  step 4. download btckeygen-master , stard to collision.

way 2:
  step 1. download all txt for this project. this is result by 1-3 step for way 1.
  step 2. download btckeygen-master , stard to collision.

Unfortunately, this project was completed in 2020. But I did not succeed in creating 0.1 BTC.
my address, 0xc84d7Bd994ca63B53c1E26Ade78BB566b8F20A1f. for eth. thanks all.
