# Comment on "Deception as Cooperation"

In [this 2019 paper](https://www.sciencedirect.com/science/article/pii/S1369848618301602) published in _Studies in History and Philosophy of Science Part C_, Manolo Martínez argues that our understanding of how communication works has been grievously impaired by philosophers not knowing enough math.

A classic [reduction](https://www.lesswrong.com/posts/p7ftQ6acRkgo6hqHb/dreams-of-ai-design) of meaning dates back to David Lewis's analysis of signaling games, [more recently elaborated on by Brian Skyrms](https://oxford.universitypressscholarship.com/view/10.1093/acprof:oso/9780199580828.001.0001/acprof-9780199580828). Two agents play a simple game: a sender observes one of several possible states of the world (chosen randomly by Nature), and sends one of several possible signals. A receiver observes the signal, and chooses one of several possible actions. The agents get a reward (as specified in a payoff matrix) based on what state was observed by the sender and what action was chosen by the receiver. This toy model explains how communication can be a thing: the incentives to choose the right action in the right state, shape [the evolution of a convention that assigns meaning to otherwise opaque signals](https://www.lesswrong.com/posts/4hLcbXaqudM9wSeor/philosophy-in-the-darkest-timeline-basics-of-the-evolution).

The math in Skyrms's presentation is simple—the information content of a signal is just how it changes the probabilities of states. _Too_ simple, according to Martínez! When Skryms and other authors (following [Fred Dreske](https://web.stanford.edu/group/cslipublications/cslipublications/site/157586195X.shtml)) use information theory, they tend to only reach for the basic probability tools you find in the _first_ chapter of the textbook. (Skyrms's _Signals_ book occasionally takes logarithms of probabilities, but the word "entropy" doesn't actually appear.) The study of information transmission only happens _after_ the forces of evolutionary game theory have led sender and receiver to choose their strategies.

Martínez thinks information theory has more to say about what kind of [cognitive work](https://www.lesswrong.com/posts/QkX2bAkwG2EpGvNug/the-second-law-of-thermodynamics-and-engines-of-cognition) evolution is accomplishing. The "State → Sender → Signals → Receiver → Action" pipeline of the Lewis–Skyrms signaling game is _exactly_ isomorphic to the "Source → Encoder → Channel → Decoder → Decoded Message" pipeline of [the noisy-channel coding theorem](https://en.wikipedia.org/wiki/Noisy-channel_coding_theorem) and other results you'd find beyond the very first chapter in the textbook. Martínez proposes we take the analogy literally: sender and receiver collude to form an information channel between states and acts.

The "channel" framing draws our attention to different aspects of the situation than the framing focused on individual signals. In particular, Skyrms wants to characterize _deception_ as being about when a sender benefits by sending a misleading signal—one that decreases the receiver's probability assigned to the true state, or increases the probability assigned to a false state.

(Actually, as [Don Fallis and Peter J. Lewis point out](http://philsci-archive.pitt.edu/13337/), Skyrms's characterization of misleadingness is too broad: one would think we wouldn't want to say that merely ruling out a false state is misleading, but it _does_ increase the probability assigned to any other false states. But let this pass for now.)

But for Martínez, a signal is just a codeword in the code being cooperatively constructed by the sender/encoder and receiver/decoder in response to the problems they jointly face.

Martínez's key later-textbook-chapter tool is [_rate–distortion theory_](https://en.wikipedia.org/wiki/Rate%E2%80%93distortion_theory). A _distortion_ measure quantifies how costly or "bad" it is to decode a given input as a given output. If the symbol was transmitted accurately, the distortion is zero; if there was some noise on the channel, then more noise is worse, although different applications can call for different distortion measures. (In audio applications, for example, we probably want a distortion measure that tracks how similar the decoded audio sounds to humans, [which could be different from the measure you'd naturally think of if you were looking at the raw bits](https://www.lesswrong.com/posts/dYspinGtiba5oDCcv/feature-selection).)

Given a choice of distortion measure, there exists a rate–distortion function $R(D)$ that, for a given level of distortion, tells us the _rate_ of how "wide" the channel needs to be in order to communicate with no more than that amount of distortion. This "width", more formally, is [channel capacity](https://en.wikipedia.org/wiki/Channel_capacity): for a particular channel (a conditional distribution of outputs given inputs), the capacity is the maximum, over possible input distributions, of the [mutual information](https://en.wikipedia.org/wiki/Mutual_information) between the input and output distributions—the most information that could possibly be sent over the channel, if we get to pick the input distribution and the code. The _rate_ is looking at "width" from the other direction: it's the _minimum_ of the mutual information between the input and output distributions, over possible _channels_ (conditional distributions) that meet the distortion goal.

What does this have to do with signaling games? Well, the payoff matrix of the game specifies how "good" it is (for each of the sender and receiver) if the receiver chooses a given act in a given state. But knowing how "good" it is to perform a given act in a given state amounts to the same thing (modulo a negative [affine transformation](https://en.wikipedia.org/wiki/Affine_transformation)) as knowing how "bad" it is for the communication channel to "decode" a given state as a given act! We can thus see the payoff matrix of the game giving us two different distortion measures, one each for the sender and receiver.

Following an old idea from Richard Blahut, we can have a rate–distortion function $R(D_S, D_R)$ with a two-dimensional domain (visualizable as a surface or heatmap) that takes as arguments a distortion target for _each_ of the two measures, and gives the minimum rate that can meet _both_. This function depends only on the distribution of states from Nature, and on the payoff matrix. The sender and receiver don't need to have already chosen their strategies for us to talk about it; rather, we can see the strategies as chosen in response to this rate–distortion landscape.

Take one of the simplest possible signaling games: three states, three signals, three acts, with sender and receiver each getting a payoff of 1 if the receiver chooses the _i_-th act in the _i_-th state for 1 ≤ _i_ ≤ 3—or rather, let's convert how-"good"-it-is payoffs, into equivalent how-"bad"-it-is distortions: sender and receiver measures both give a distortion of 1 when the _j_-th act is taken in the _i_-th state for _i_ ≠ _j_, and 0 when _i_ = _j_. 

This rate–distortion function characterizes the outcomes of possible behaviors in the game. The fact that $R(\frac{2}{3}, \frac{2}{3}) = 0$ means that a distortion of $\frac{2}{3}$ can be achieved without communicating at all. (Just guess.) The fact that $D(0, 0) = \lg 3$ means that, to communicate perfectly, the sender/encoder and receiver/decoder need to form a channel/code whose rate matches the entropy of the three states of nature.

But there's a continuum of possible intermediate behaviors: consider the ["trembling hand"](https://en.wikipedia.org/wiki/Trembling_hand_perfect_equilibrium) strategy, under which the sender sends the _i_-th signal and the receiver chooses the _j_-th act with probability $1 - p$ when _i_ = _j_, but probability $\frac{p}{2}$ when _i_ ≠ _j_. Then the mutual information between states and acts would be $(1 - p) \lg \frac{1}{1 - p} + p \lg \frac{2}{p}$, smoothly interpolating between the perfect-signaling case and the no-communication-just-guessing case.

This introductory case of perfect commmon interest is pretty boring. Where the rate–distortion framing really shines is in analyzing games of _imperfect_ common interest, where sender and receiver can benefit from communicating _at all_, but also have a motive to fight about exactly what to communicate. To illustrate his account of deception, Skryms considers a three-state, three-act game with the following payoff matrix, where the rows represent states and the columns represent actions, and the payoffs are given as (sender's payoff, receiver's payoff)—

$$ \begin{matrix}2,10 & 0,0 & 10,8 \cr 0,0 & 2,10 & 10,8 \cr 0,0 & 10,10 & 0,0 \end{matrix} $$

(Note that this payoff matrix is _not_ a [normal-form game matrix](https://en.wikipedia.org/wiki/Normal-form_game) in which the rows and columns represent would represent player strategy choices; the sender's choice of what signal to send is not depicted.)









https://www.lesswrong.com/posts/ybG3WWLdxeTTL3Gpd/communication-requires-common-interests-or-differential
https://www.lesswrong.com/posts/YptSN8riyXJjJ8Qp8/maybe-lying-can-t-exist

https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception
https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting
