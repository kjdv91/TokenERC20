from brownie import accounts, config, TokenImport

initialSupply = 100000000000000000
tokenName = "TOCOIN"
tokenSymbol = "KJDV"


def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = TokenImport.deploy(
        initialSupply, tokenName, tokenSymbol, {"from": account}, publish_source=True
    )
