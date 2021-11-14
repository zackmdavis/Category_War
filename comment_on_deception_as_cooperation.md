# Comment on "Deception as Cooperation"

In [this 2019 paper](https://www.sciencedirect.com/science/article/pii/S1369848618301602) published in _Studies in History and Philosophy of Science Part C_, Manolo Martínez argues that our understanding of how communication works has been grievously impaired by philosophers not knowing enough math.

A classic [reduction](https://www.lesswrong.com/posts/p7ftQ6acRkgo6hqHb/dreams-of-ai-design) of meaning dates back to David Lewis's analysis of signaling games, [more recently elaborated on by Brian Skyrms](https://oxford.universitypressscholarship.com/view/10.1093/acprof:oso/9780199580828.001.0001/acprof-9780199580828). Two agents play a simple game: a sender observes one of several possible states of the world (chosen randomly by Nature), and sends one of several possible signals. A receiver observes the signal, and chooses one of several possible actions. The agents get a reward (as specified in a payoff matrix) based on what state was observed by the sender and what action was chosen by the receiver. This toy model explains how communication can be a thing: the incentives to choose the right action in the right state, shape [the evolution of a convention that assigns meaning to otherwise opaque signals](https://www.lesswrong.com/posts/4hLcbXaqudM9wSeor/philosophy-in-the-darkest-timeline-basics-of-the-evolution).

The math in Skyrms's presentation is simple—the information content of a signal is just how it changes the probabilities of states. _Too_ simple, according to Martínez! When Skryms and other authors (following [Fred Dreske](https://web.stanford.edu/group/cslipublications/cslipublications/site/157586195X.shtml)) use information theory, they tend to only reach for the basic probability tools you find in the _first_ chapter of the textbook. (Skyrms's _Signals_ book occasionally takes logarithms of probabilities, but the word "entropy" doesn't actually appear.) The study of information transmission only happens _after_ the forces of evolutionary game theory have led sender and receiver to choose their strategies.

Martínez thinks information theory has more to say about what kind of cognitive work evolution is accomplishing. The "State → Sender → Signals → Receiver → Act" pipeline of the Lewis–Skyrms signaling game is _exactly_ isomorphic to the "Source → Encoder → Channel → Decoder → Decoded Message" pipeline of [the noisy-channel coding theorem](https://en.wikipedia.org/wiki/Noisy-channel_coding_theorem) and other results you'd find beyond the very first chapter in the textbook. Martínez proposes we take the analogy literally: the sender and receiver collude to form an information channel between states and acts.

The "channel" framing draws our attention to different aspects of the model than the framing focused on individual signals. In particular, Skyrms wants to characterize _deception_ as being about when a sender benefits by sending a misleading signal—one that decreases the receiver's probability assigned to the true state, or increases the probability assigned to a false state. (Actually, as [Don Fallis and Peter J. Lewis point out](http://philsci-archive.pitt.edu/13337/), Skyrms's characterization of misleadingness is too broad: one would think we wouldn't want to say that merely ruling out a false state is misleading, but it _does_ increase the probability assigned to any other false states. But let this pass for now.) But for Martínez, a signal is just a codeword in the code being cooperatively constructed by the sender/encoder and receiver/decoder in response to the problems they jointly face.

In the case of perfect common interest

Rate–distortion theory








https://www.lesswrong.com/posts/ybG3WWLdxeTTL3Gpd/communication-requires-common-interests-or-differential
https://www.lesswrong.com/posts/YptSN8riyXJjJ8Qp8/maybe-lying-can-t-exist

https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception
https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting
