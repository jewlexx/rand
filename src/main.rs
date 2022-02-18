use num_cpus::get as get_cpus;

fn main() {
    let cpus = get_cpus();

    let pool = threadpool::Builder::new();
}
