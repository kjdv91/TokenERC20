//SPDX-License-Identifier:MIT
pragma solidity ^0.8.10;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Token is ERC20 {
    constructor() ERC20("HEVADA", "KJDV") {
        _mint(msg.sender, 2000);
    }
}
