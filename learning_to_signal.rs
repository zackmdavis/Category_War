#!/usr/bin/env run-cargo-script
// cargo-deps: rand="0.7"

// Use cargo-script (https://github.com/DanielKeep/cargo-script) to run as a
// standalone script.

use std::collections::HashMap;

extern crate rand;
use rand::distributions::{Distribution, Uniform};
use rand::seq::SliceRandom;
use rand::thread_rng;

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

#[derive(Debug)]
struct Sender {
    policy: HashMap<(State, Signal), u32>,
}

impl Sender {
    fn new() -> Self {
        let mut sender = Self {
            policy: HashMap::new(),
        };
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

    fn reinforce(&mut self, state: State, signal: Signal) {
        *self.policy.entry((state, signal)).or_insert(0) += 1;
    }
}

#[derive(Debug)]
struct Reciever {
    policy: HashMap<(Signal, Action), u32>,
}

impl Reciever {
    fn new() -> Self {
        let mut sender = Self {
            policy: HashMap::new(),
        };
        for &signal in &[Signal::S1, Signal::S2] {
            for &action in &[Action::BundleUp, Action::StripDown] {
                sender.policy.insert((signal, action), 1);
            }
        }
        sender
    }

    fn act(&self, signal: Signal) -> Action {
        let bundle_potential = self.policy.get(&(signal, Action::BundleUp)).unwrap();
        let strip_potential = self.policy.get(&(signal, Action::StripDown)).unwrap();

        let mut randomness_source = thread_rng();
        let distribution = Uniform::new(0, bundle_potential + strip_potential);
        let roll = distribution.sample(&mut randomness_source);
        if roll < *bundle_potential {
            Action::BundleUp
        } else {
            Action::StripDown
        }
    }

    fn reinforce(&mut self, signal: Signal, action: Action) {
        *self.policy.entry((signal, action)).or_insert(0) += 1;
    }
}

fn main() {
    let mut sender = Sender::new();
    let mut reciever = Reciever::new();
    let states = [State::Hot, State::Cold];
    for _ in 0..10000 {
        let mut randomness_source = thread_rng();
        let state = *states.choose(&mut randomness_source).unwrap();
        let signal = sender.send(state);
        let action = reciever.act(signal);
        match (state, action) {
            (State::Hot, Action::StripDown) | (State::Cold, Action::BundleUp) => {
                sender.reinforce(state, signal);
                reciever.reinforce(signal, action);
            }
            _ => {}
        }
    }
    println!("{:?}", sender);
    println!("{:?}", reciever);
}
