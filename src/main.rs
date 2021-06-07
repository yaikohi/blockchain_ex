use sha2::{Digest, Sha256, digest::Update};
use std::{u64, vec::Vec};

// https://doc.rust-lang.org/std/hash/index.html

#[derive(Debug)]
struct BlockHash {
    block_hash: u64,
}

#[derive(Debug)]
struct ExampleCoinBlock {
    previous_block_hash: String,
    transaction_list: Vec<String>,
    block_hash: Sha256,
}

impl ExampleCoinBlock {
    pub fn new(
        previous_block_hash_value: String,
        transaction_list_value: Vec<String>,
        block_hash_value: Sha256,
    ) -> Self {
        Self {
            previous_block_hash: previous_block_hash_value,
            transaction_list: transaction_list_value,
            block_hash: block_hash_value,
        }
    }
    pub fn update_block_hash(&self) -> Self {
        &self.transaction_list.push(self.previous_block_hash);

        let block_data = self.transaction_list.join("-");

        let mut hash = Sha256::new();
        hash.update(block_data);
        hash.finalize();

        Self {
            previous_block_hash: "".to_string(),
            transaction_list: vec!["hei".to_string()],
            block_hash: hash,
        }
    }
}

// type BlockHashT<'a> = &'a str;

fn main() {
    let first_coin_block = ExampleCoinBlock {
        previous_block_hash: "Initial string".to_string(),
        transaction_list: vec!["T1".to_string(), "T2".to_string()],
        block_hash: Sha256::new(),
    };

    let second_coin_block = ExampleCoinBlock::new(
        first_coin_block.previous_block_hash,
        vec!["T3".to_string(), "T4".to_string()],
        Sha256::new(),
    );

    println!("{:?}", first_coin_block.transaction_list);
    println!("{:?}", second_coin_block.previous_block_hash);
    println!("{:?}", second_coin_block.update_block_hash())
}
