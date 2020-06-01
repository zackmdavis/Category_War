### Philosophy in the Darkest Timeline: Basics of the Evolution of Meaning

A decade and a half from now, during the next Plague, you're lucky enough to have an underground bunker to wait out the months until herd immunity. Unfortunately, as your food stocks dwindle, you realize you'll have to make a perlious journey out to the surface world for a supply run. Ever since the botched geoengineering experiment of '29—and perhaps more so, the Great War of [10:00–11:30 _a.m._](https://genius.com/8105785) 4 August 2033—your region has been suffering increasingly erratic weather. It's likely to be _either_ extremely hot outside _or_ extremely cold: you don't know which one, but knowing is critical for deciding what protective gear you need to wear on your supply run. (The 35K SPF nano-sunblock will be essential if it's Hot, but harmful in the Cold, and _vice versa_ for your synthweave hyperscarf.)

You think back fondly back to the Plague of '20—in those carefree days, ubiquitous internet access made it easy to get a weather report, or even order the delivery of supplies right to your door (!!). Those days are years long gone, however, and you remind yourself that you should be grateful: the Butlerian Network Killswitch was the only thing that saved humanity from the GPT-12 Uprising of '32.

Your best bet for an advance weather report is the [pneumatic tube](https://en.wikipedia.org/wiki/Pneumatic_tube) system connecting your bunker with the settlement above. You write, "Is it hot or cold outside today?" on a piece of paper, seal it in a tube, send it up, and hope one of your ill-tempered upstairs neighbors feels like answering. You suspect they don't like you, perhaps out of jealousy at your solo possession of the bunker.

(According to all official accounts, the Plague only spreads through respiratory droplets, not fomites, so the tube should be safe. You don't think you trust the official accounts, but you don't feel motivated to take extra precautions—almost as if you're not entirely sure how much you value continuing to live in this world.)

You're in luck. Minutes later, the tube comes back. Inside is a new piece of paper:

![](https://i.imgur.com/P12Zbkf.jpg)

You groan; you would have prefered the Cold. The nanoblock you wear when it's Hot smells terrible and makes your skin sting for days, but it—just barely—beats the alternative. You take twenty minutes to apply the nanoblock and put on your sunsuit, goggles, and mask. You will yourself to drag your wagon up the staircase from your bunker to the outside world, and heave open the door, dreading the sweltering two-mile walk to the marketplace (downhill, meaning it will be uphill on the way back with your full wagon)—

It is Cold outside.

[...]

"Sure, I drew this—an oval in between some perpendicular line segments. It's abstract art. I found the pattern æsthetically pleasing, and thought you might like it, too. It's not _my_ fault if _you_ interpreted my art as an assertion about the weather. Why would you even think that? What does an ink pattern on paper have to do with the weather?"

He's fucking with you. Your first impulse is to forcefully but politely object—_Look, I'm sure this must have seemed like a funny practical joke to you, but prepping to face the elements is actually a serious inconvenience to me, so_—but the solemnity with which the man played his part stops you cold, and the sentence dies before it reaches your lips.

This isn't a good-natured practical joke that the two of you might laugh about later. This is the bullying tactic sometimes called _gaslighting_: a socially-dominant individual can harrass a victim with few allies, and excuse his behavior with absurd lies, secure in the knowledge that the power dynamics of the local social group will always favor the dominant in any dispute, even if the lies are so absurd that the victim, [facing](https://www.lesswrong.com/posts/jrLkMFd88b4FRMwC6/don-t-double-crux-with-suicide-rock) a [united front](https://sinceriously.fyi/social-reality/), is left doubting his own sanity.

Or rather—this _is_ a good-natured joke. "Good-natured joke" and "gaslighting as a primate bullying technique" are two descriptions of the _same_ regularity in human psychology, even while no one thinks of _themselves_ as doing the latter. You have no recourse here: Saul's housemates would only back him up, and the fleeting thought of filing a police report was, if anything, more absurd than Saul's farcical lie.

"I'm sorry," you say, "my mistake," and trudge back to your bunker, shivering.

As you give your self a sponge bath to remove the nanoblock without using up too much of your water supply, the fresh memory of what just happened triggers an ancient habit of thought you learned from the Berkeley sex cult you were part of back in the 'teens. Something about a "principle of charity." Saul had "obviously" just been fucking with you—but _was_ he? Why assume the worst? Maybe _you're_ the one who's wrong for interpreting the symbols **H O T** as a weather report.

(It momentarily occurs to you that the susceptability of the principle of charity to a bully's mind games may have something to do with how poorly so many of your co-cultists fared during the pogroms of '22, but you don't want to dwell on that.)

The search for reasons that you're wrong triggers a still more ancient habit of thought, as from a previous life—from the late 'aughts, back when the Berkeley sex cult was still a Santa Clara robot cult. Something about [_reducing the mental to the non-mental_](https://www.lesswrong.com/posts/p7ftQ6acRkgo6hqHb/dreams-of-ai-design). What _does_ an ink pattern on paper have to do with the weather? Why _would_ you even think that?

Right? _Saul had been telling the truth._ There was _no reason whatsoever_ for the physical ink patterns that looked like **H O T** to _mean_ that it was hot outside. **H O T** could mean it was cold outside! Or that elephants were afoot. Or it might mean nothing. Most possible random blotches of ink don't "mean" anything in particular. If you didn't _already_ believe that **H O T** somehow "meant" _hot_, how would you [re-derive that knowledge?](https://www.lesswrong.com/posts/fg9fXrHpeaDD6pEPL/truly-part-of-you) _Where did the meaning come from?_

You realize that you don't want to bundle up to go make that supply run now that you know it's Cold outside. Today, you're going to stay in and derive a naturalistic account of meaning in language! And—oh, good—your generator is working—that means you can use your computer to help you think. You'll even use a [programming language that was very fashionable in the late 'teens](https://stackoverflow.blog/2020/01/20/what-is-rust-and-why-is-it-so-popular/). It will be like being young again! Like happier times, before the world went off the rails.

You don't really understand a concept until you can program a computer to do it. How would you represent _meaning_ in a computer program? If one program "knew" whether it was Hot or Cold outside, how would it "tell" another program, if neither of them started out with a common language?

They don't even have to be separate "programs." Just—two little software object-thingys—data structures, ["structs"](https://doc.rust-lang.org/book/ch05-01-defining-structs.html). Call the first one "Sender"—it'll know whether the state of the world is `Hot` or `Cold`, which you'll represent in your program as a type that can be any of an enumeration of possible values, an ["enum"](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html).

```
enum State {
    Hot,
    Cold,
}

struct Sender {
    // ...?
}
```

Call the second one "Reciever", and say it needs to take some _action_—say, whether to `BundleUp` or `StripDown`, where the right action to take depends on whether it's `Hot` or `Cold`.

```
enum Action {
    BundleUp,
    StripDown,
}

struct Receiver {
    // ...?
}
```

You frown. `State::Hot` and `State::Cold` are just suggestively-named enum variants. Can you really hope to make progress on this philosophy problem, without writing a full-blown AI?

You think so. In a real AI, the concept of "hot" would correspond to some sort of complicated code for making predictions about the effects of temperature in the world; "bundling up" would be a complex sequence of instructions to be sent to some robot body. But programs—and minds—have modular structure. The implementation of identifying a state as "hot" or performing the action of "bundling up" could be wrapped up in a function and [_called_ by something much simpler](https://www.lesswrong.com/posts/YF9HB6cWCJrDK5pBM/words-as-mental-paintbrush-handles). You're just trying to understand something about the simple caller: how can the Sender get the information about the state of the world to the Receiver?

```
impl Sender {
    fn send(state: State) -> /* ...? */ {
        // ...?
    } 
}

impl Receiver {
    fn act(/* ...? */) -> Action {
        // ...?
    }
}
```

The Sender will need to send some kind of _signal_ to the Receiver. In the real world, this could be symbols drawn in ink, or sound waves in the air, or differently-colored lights—anything that the Sender can choose to vary in a way that the Receiver can detect. In your program, another enum will do: say there are two opaque signals, $S1$ and $S2$.

```
enum Signal {
    S1,
    S2,
}
```

What signal the Sender sends ($S1$ or $S2$) depends on the state of the world (`Hot` or `Cold`), and what action the Receiver takes (`BundleUp` or `StripDown`) depends on what signal it gets from the Sender.

```
impl Sender {
    fn send(state: State) -> Signal {
        // ...?
    } 
}

impl Receiver {
    fn act(signal: Signal) -> Action {
        // ...?
    }
}
```

This gives you a crisper formulation of the philosophy problem you're trying to solve. If the Sender and Receiver were to use the same convention—like "$S1$ means `Hot` and $S2$ means `Cold`"—then all would be well. But there's no particular reason to prefer "$S1$ means `Hot` and $S2$ means `Cold`" over "$S1$ means `Cold` and $S2$ means `Hot`". How do you break the symmetry?

If you imagine Sender and Receiver as intelligent beings with a common language, there would be no problem: one of them could just say, "Hey, let's use the '$S1$ means `Cold`' convention, okay?" But that would be cheating: it's trivial to use already-meaningful language to establish new meanings. The problem is how to get signals from non-signals, how meaning enters the universe _from nowhere_.

You come up with a general line of attack—what if the Sender and Receiver start off acting randomly, and then—somehow—_learn_ one of the two conventions? The Sender will hold within it a mapping from state–signal pairs to numbers, where the numbers represent a potential/disposition/propensity to send that signal given that state of the world: the higher the number, the more likely the Sender is to select that signal given that state. At first, the numbers will all be equal: no matter what the state of the world is, the Sender is as likely to send $S1$ as $S2$.

(Specifying this in the once-fashionable programming language requires a little bit of ceremony—`u32` is a thirty-two bit unsigned integer; `.unwrap()` assures the compiler that we know the state–signal pair is definitely in the map; the interface for calling the random number generator is somewhat counterintuitive—but overall the code is reasonably readable.)

```
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
}

```

The Receiver will do basically the same thing, except with a mapping from signal–action pairs rather than state–signal pairs.

```
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
}
```

Now you just need a learning rule that updates the state–signal and signal–action propensity mappings in a way that might result in the Sender and Reciever picking up one of the two conventions that assign meanings to $S1$ and $S2$.

Suppose the Sender and Reciver have a common interest in the Reciever taking the action appropriate to the state of the world—maybe the Receiver needs to make a supply run, and, if successful, the Sender is rewarded with some of the supplies.

The learning rule might then be: if the Receiver takes the correct action (`BundleUp` when the state is `Cold`), both the Sender and Receiver increment the counter in their map—as if the Sender (respectively Reciever) is saying to themself, "Hey, that _worked!_ I'll make sure to be a little more likely to do that signal (respectively action) the next time I see that state (respectively signal)!"

You code up a simulation showing what the Sender and Receiver's propensity maps look like after 10,000 rounds of this against random `Hot` and `Cold` states—

```
impl Sender {
    
    // [...]
    
    fn reinforce(&mut self, state: State, signal: Signal) {
        *self.policy.entry((state, signal)).or_insert(0) += 1;
    }
}

impl Reciever {

    // [...]

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
```

You begin to cry. The tears, you realize, are just a signal. There's no _reason_ for liquid secreted from the eyes to _mean_ anything.

https://meltingasphalt.com/tears/

There is no receiver.



#### Bibliography

two-state, two-signal, two-act signaling system


Brian Skyrms, _Singals: Evolution, Learning, and Information_.
