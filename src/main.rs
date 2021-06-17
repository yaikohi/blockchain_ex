use std::vec::Vec;
use sha2::{ Digest, Sha256 };

struct ExampleCoinBlock {
    previous_block_hash: String,
    transaction_list: Vec<String>,
}
// type BlockHashT = ArrayLength<u8>;

impl ExampleCoinBlock {
    fn new(prev_blockhash: String, trans_list: Vec<String>) -> ExampleCoinBlock {
        ExampleCoinBlock { 
            previous_block_hash: prev_blockhash, 
            transaction_list: trans_list, 
        }
    }
    
    fn create_block_hash(mut trans_list: Vec<String>, prev_blockhash: String) -> sha2::Sha256 {
        // let block_data: Vec<String>;
        trans_list.push(prev_blockhash);

        let block_data = trans_list.join("-");
        let mut block_hash = Sha256::new();
        block_hash.update(&block_data);
        block_hash.finalize();
        
        block_hash
    }
}

fn main() {
    let first_coin = ExampleCoinBlock {
        previous_block_hash: "Initial string".to_string(),
        transaction_list: vec!["T1".to_string(), "T2".to_string()],
    };
    println!("{:?}", first_coin.transaction_list)
}
