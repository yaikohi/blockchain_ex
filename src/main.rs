use std::vec::Vec;
use sha2::{ Digest, Sha256, Sha512 };

// https://doc.rust-lang.org/std/hash/index.html
use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};



struct ExampleCoinBlock <'a> {
    previous_block_hash: &'a str,
    transaction_list: Vec<String>,
}

type BlockHashT<'a> = &'a str;


impl ExampleCoinBlock<'_> {
    pub fn new() -> ExampleCoinBlock<'_> {
        ExampleCoinBlock {
            previous_block_hash,
            transaction_list,
        }
    }
    
    fn create_block_hash(&self) -> <BlockHashT> {
        let block_data = &self.transaction_list
            .push(&self.previous_block_hash)
            .join("-");
        let block_hash = Sha256::new()
            .update(block_data)
            .finalize();
        block_hash
    }
}

fn main() {
    let first_coin = ExampleCoinBlock {
        previous_block_hash: "Initial string",
        transaction_list: vec!["T1".to_string(), "T2".to_string()],
    };
    println!("{:?}", first_coin.transaction_list)
}
