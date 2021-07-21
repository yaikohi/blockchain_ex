use std::time::{Duration, SystemTime};
use std::thread::sleep;

struct Blockchain{
    chain: vec![],
    genesis_block: any,
}

struct Block {
    verified_transactions: vec![],
    previous_block_hash: String,
    nonce: String,
}

impl Blockchain {
    fn new() -> Self {
        Self {
            vec![0],
            Block {
                verified_transactions: vec![0],
                previous_block_hash: SystemTime::now(),
                nonce: "nonceee",
            }
        }
    }
    fn create_genesis_block(self) -> self {
        genesis_block = Block {
            verified_transactions: vec![0],
            previous_block_hash: SystemTime::now(),
            nonce: "0",
        }
    }
}