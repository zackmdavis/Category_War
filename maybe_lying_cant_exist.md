## Maybe Lying Can't Exist?!

How is it possible to tell the truth? I mean, sure, you can use your larynx to make sound waves in the air, or draw a sequence of symbols on paper, but sound waves can't be _true_, any more than a leaf or a rock can be "true". Why do you [think you can](https://www.lesswrong.com/posts/rQEwySCcLtdKHkrHp/righting-a-wrong-question) tell the truth?

This is a pretty easy question. Words don't have intrinsic ontologically-basic meanings, but intelligent systems can _learn_ associations between a symbol and things in the world. If I say "dog" and point to a dog a bunch of times, a child who didn't already know what the word "dog" meant, would get the idea and learn that the sound "dog" _meant_ this-and-such kind of furry four-legged animal.

As a _formal_ model of how this AI trick works, [we can study sender–receiver games](https://www.lesswrong.com/posts/4hLcbXaqudM9wSeor/philosophy-in-the-darkest-timeline-basics-of-the-evolution). Two agents play a simple game: a sender observes one of several possible states of the world, and sends one of several possible signals. A receiver observes the signal, and chooses one of several possible actions. If the agents get rewarded when the state of the world the sender saw "matches" the action the receiver chose, a convention evolves that assigns meanings to the previously and otherwise arbitrary signals. True information is communicated; the signals become a _shared_ map that reflects the territory.

How is it possible to _lie_?

This is ... a surpisingly less easy question. The problem is that, in the framework of the sender–receiver game, the meaning of a signal is simply how it makes a receiver update its probabilities, which is determined by the conditions under which the signal is sent. If I say "dog" and four-fifths of the time I point to a dog, but one-fifth of the time I point to a tree, what should a child conclude? Does "dog" mean dog-with-probability-0.8-and-tree-with-probability-0.2, or does "dog" mean dog, and I'm just lying one time out of five? Our sender–receiver game model would seem to favor the former interpretation.

What could make a signal _deceptive_?

Traditionally, _deception_ has been regarded as intentionally causing someone to have a false belief. As Bayesians, however, we prefer not to grapple with anthropmorphic black boxes like "intent" and "belief." As part of a _first attempt_ at making sense of deceptive signaling, let's generalize "causing someone to have a false belief" to "causing the reciever to update its probability distribution to be less accurate (as defined by [the logarithm of the probability it assigns to the true state](https://www.lesswrong.com/posts/afmj8TKAqH6F2QMfZ/a-technical-explanation-of-technical-explanation))", and [generalize "intentionally" to](https://www.lesswrong.com/posts/sXHQ9R5tahiaXEZhR/algorithmic-intent-a-hansonian-generalized-anti-zombie) "benefitting the sender (as defined by rewards in the sender–receiver game)".

One might ask: why require the sender to benefit in order for a signal to count as deceptive? Why isn't "made the receiver update in the wrong direction" enough?

The answer is that we're seeking an explanation for communication that _systematically_ makes receivers update in the wrong direction—signals that we can think of as having been _optimized for_ deception, rather than accidentally happening to mislead on this particular occasion. The "rewards" in this model should be interpreted mechanistically, not necessarily mentalistically. It's _just_ that things that get "rewarded" more, happen more often. That's all—and that's enough to shape the evolution of how the system processes information. There need not be any conscious mind that "feels happy" about getting rewarded (although that implementation, among many possible alternatives, would do the trick).



-----

### Bibliography

This post presents ideas covered in these works—

Fallis, Don and Lewis Peter J., ["Toward a Formal Analysis of Deceptive Signaling"](http://philsci-archive.pitt.edu/13337/)

Skyrms, Brian and Barrett, Jeffrey A., ["Propositional Content in Signals"](http://philsci-archive.pitt.edu/14774/)

Skyrms, Brian, _Signals: Evolution, Learning, and Information_, Ch. 6, "Deception"
