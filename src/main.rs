use sha2::{Digest, Sha256, Sha512};
use std::vec::Vec;

// https://doc.rust-lang.org/std/hash/index.html
use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};

struct ExampleCoinBlock {
    previous_block_hash: &str,
    transaction_list: Vec<String>,
    block_data: String,
    block_hash: u64,
}

impl ExampleCoinBlock {
    fn create_block_hash(&self) -> GenericArray<u8> {
        let mut hasher = Sha256::new();
        hasher.update(self.block_data);
        let result = hasher.finalize();
        println!("{:?}", result)
    }
}
fn main() {
    println!("Hello, world!");
    let first_coin = ExampleCoinBlock {
        previous_block_hash: "Initial string",
        transaction_list: vec!["T1".to_string(), "T2".to_string()],
        block_data: self.transaction_list.join("-") + "-" + self.previous_block_hash,
        block_hash: Sha256::new().update(self.block_data).finalize(),
    };
}
