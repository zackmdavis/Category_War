#!/usr/bin/env run-cargo-script
// cargo-deps: rand="0.7"

use std::collections::HashMap;

extern crate rand;
use rand::{Rng, thread_rng};
use rand::distributions::Uniform;
use rand::distributions::Distribution;


#[derive(Copy, Clone, PartialEq, Eq, Hash, Debug)]
enum State {
    Hot,
    Cold,
}

#[derive(Copy, Clone, PartialEq, Eq, Hash, Debug)]
enum Signal {
    S1,
    S2,
}

#[derive(Copy, Clone, PartialEq, Eq, Hash, Debug)]
enum Action {
    BundleUp,
    StripDown,
}

struct Sender {
    policy: HashMap<(State, Signal), u32>
}

impl Sender {
    fn new() -> Self {
        let mut sender = Self { policy: HashMap::new() };
        for &state in &[State::Hot, State::Cold] {
            for &signal in &[Signal::S1, Signal::S2] {
                sender.policy.insert((state, signal), 1);
            }
        }
        sender
    }

    fn send(&self, state: State) -> Signal {
        let s1_potential = self.policy.get(&(state, Signal::S1)).unwrap();
        let s2_potential = self.policy.get(&(state, Signal::S2)).unwrap();

        let mut randomness_source = thread_rng();
        let distribution = Uniform::new(0, s1_potential + s2_potential);
        let roll = distribution.sample(&mut randomness_source);
        if roll < *s1_potential {
            Signal::S1
        } else {
            Signal::S2
        }
    }
}

struct Reciever {
    policy: HashMap<(Signal, Action), u32>
}



fn main() {
    let sender = Sender::new();
    for _ in 0..20 {
        println!("{:?}", sender.send(State::Hot));
    }
    println!("Hello signaling world");
}
