use num_cpus::get as get_cpus;
use std::{
    ops::Range,
    u128::{MAX, MIN},
};

const RANGE: Range<u128> = MIN..MAX;

fn main() {
    let cpus = get_cpus();
    let pool = threadpool::Builder::new();
}
