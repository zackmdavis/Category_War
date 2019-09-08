## Heads I Win, Tails?—Never Heard of Her; Or, Blatant Cherry-Picking Is the Best Kind

**Followup to:** [What Evidence Filtered Evidence?](https://www.lesswrong.com/posts/kJiPnaQPiy4p9Eqki/what-evidence-filtered-evidence), [Blatant Lies Are the Best Kind!](https://www.lesswrong.com/posts/KzAG4yWQJosmEjHe2/blatant-lies-are-the-best-kind) 

In ["What Evidence Filtered Evidence?"](https://www.lesswrong.com/posts/kJiPnaQPiy4p9Eqki/what-evidence-filtered-evidence), we are asked to consider a scenario involving a coin that is _either_ biased to land Heads 2/3rds of the time, _or_ Tails 2/3rds of the time. Observing Heads is 1 bit of evidence for the coin being Heads-biased (because the Heads-biased coin lands Heads with probability 2/3, the Tails-biased coin does so with probability 1/3, the likelihood ratio of these is $\frac{2/3}{1/3} = 2$, and $\log_{2} 2 = 1$), and analogously and respectively for Tails.

If such a coin is flipped ten times by someone who [doesn't make literally false statements](https://www.lesswrong.com/posts/xdwbX9pFEr7Pomaxv/meta-honesty-firming-up-honesty-around-its-edge-cases), who then reports that the 4th, 6th, and 9th flips came up Heads, then the update to our beliefs about the coin depends on what _algorithm_ the not-lying[^honest] reporter used to decide to report those flips in particular. If they always report the 4th, 6th, and 9th flips _independently_ of the flip outcomes—if there's no [evidential entanglement](https://www.lesswrong.com/posts/6s3xABaXKPdFwA3FS/what-is-evidence) between the flip outcomes and the choice of which flips get reported—then reported flip-outcomes can be treated the same as flips you observed yourself: three Headses is 3 * 1 = 3 bits of evidence in favor of the hypothesis that the coin is Heads-biased. (So if we were initially 50:50 on the question of which way the coin is biased, our posterior odds after collecting 3 bits of evidence for a Heads-biased coin would be $2^3:1$ = 8:1, or a probability of 8/(1 + 8) ≈ 0.89 that the coin is Heads-biased.)

[^honest]: I don't quite want to use the word _honest_ here.

On the other hand, if the reporter mentions only and exactly the flips that came out Heads, then we can _infer_ that the other 7 flips came out Tails (if they didn't, the reporter would have mentioned them), giving us posterior odds of $2^3:2^7$ = 1:16, or a probability of around 0.06 that the coin is Heads-biased.

So far, so standard. (You _did_ [read the Sequences](https://www.readthesequences.com/), right??) What I'd like to _emphasize_ about this scenario today, however, is that while a Bayesian reasoner who _knows_ the non-lying reporter's algorithm of what flips to report will never be misled by the selective reporting of flips, a Bayesian with _mistaken_ beliefs about the reporter's decision algorithm can be misled _quite badly_: compare the 0.89 and 0.06 probabilities we just derived given the _same_ reported outcomes, but different assumptions about the reporting algorithm.

If the coin gets flipped a sufficiently large number of times, a reporter who you _trust_ to be impartial (but isn't), can _make you believe anything she wants without ever telling a single lie_, just with appropriate selective reporting. Imagine a _very_ biased coin that comes up Heads 99% of the time. If it gets flipped a ten thousand times, 100 of those flips will be Tails (in expectation), giving a selective reporter plenty of examples to point to if she wants to convince you that the coin is extremely Tails-biased.

Toy models about biased coins are instructive for constructing examples with explicitly calculable probabilities, but the same _structure_ applies to any real-world situation where you're receiving evidence from other agents, and you have uncertainty about what algorithm is being used to determine what reports get to you. Reality is like the coin's bias; evidence and arguments are like the outcome of a particular flip. _Wrong_ theories will still have _some_ valid arguments and evidence supporting them (as even a very Heads-biased coin will come up Tails sometimes), but theories that are [_less_ wrong](https://tvtropes.org/pmwiki/pmwiki.php/Main/TitleDrop) will have _more_.

If selective reporting is mostly due to the idiosyncratic [bad intent](http://benjaminrosshoffman.com/bad-faith-behavior-not-feeling/) of rare malicious actors, then you might hope for safety in [(the law of large)](TODO: linky) numbers: if Helga in particular is systematically more likely to report Headses than Tailses that she sees, then her flip reports will diverge from everyone else's, and you can _take that into account_ when reading Helga's reports. On the other hand, if selective reporting is mostly due to systemic _structural_ factors that result in _correlated_ selective reporting even among well-intentioned people who are being honest as best they know how,[^how] then you might have a more serious problem.

[^how]: And it turns out that knowing _how_ to be honest is _much more work_ than one might initially think. You _have_ [read the Sequences](https://www.readthesequences.com/), right?!

["A Fable of Science and Politics"](https://www.lesswrong.com/posts/6hfGNLf4Hg5DXqJCF/a-fable-of-science-and-politics) depicts a fictional underground Society polarized between two partisan factions, the Blues and the Greens. "[T]here is a 'Blue' and a 'Green' position on almost every contemporary issue of political or cultural importance." If human brains consistently understood the is/ought distinction, then political or cultural alignment with the Blue or Green agenda wouldn't distort people's beliefs about reality. Unfortunately ... humans. (I'm not even going to finish the sentence.)

Reality itself isn't on anyone's side, but any particular fact, argument, [sign, or portent](TODO: bottom line) might just so happen to be more easily construed as "supporting" the Blues or the Greens. The Blues support stronger marriage laws; the Greens support no-fault divorce. An [evolutionary psychologist](https://www.lesswrong.com/posts/epZLSoNvjW53tqNj9/evolutionary-psychology) investigating [effects of kin-recognition mechanisms on child abuse by stepparents](https://en.wikipedia.org/wiki/Cinderella_effect) might aspire to scientific objectivity, but being objective and _staying_ objective is _difficult_ when you're embedded in an [intelligent social web](https://www.lesswrong.com/posts/AqbWna2S85pFTsHH4/the-intelligent-social-web) in which in your work is going to be predictably championed by Blues and reviled by Greens.

Let's make another toy model to try to understand the resulting distortions on the Undergrounders' collective epistemology. Suppose Reality is a coin—no, not a coin, a three-sided die,[^triangle] with faces colored blue, green, and gray. One-third of the time it comes up blue (representing a fact that is more easily construed as supporting the Blue narrative), one-third of the time it comes up green (representing a fact that is more easily construed as supporting the Green narrative), and one-third of the time it comes up gray (representing a fact that not even the worst ideologues know how to spin as "supporting" their side). 

[^triangle]: For lack of an appropriate [Platonic solid](https://en.wikipedia.org/wiki/Platonic_solid) in three-dimensional space, maybe imagine tossing a triangle in two-dimensional space??

Suppose each faction enforces consensus internally. [Without loss of generality](TODO: link), take the Greens.[^choice] 

[^choice]: As an author, I'm facing some conflicting desiderata in my color choices here. I want to say "Blues and Greens" _in that order_ for compatibility with "A Fable of Science and Politics" (and other [classics from the Sequences](TODO: linky Blue or Green on regulation)). Then when making an arbitrary choice to talk in terms of the factions in order to avoid cluttering the dialogue when it's understood that all the same considerations apply to the other faction, you might expect me to say "Without loss of generality, take the Blues," because the first item in "Blues and Greens" is a more obvious Schelling point 








anyone who's actually [paying attention](https://srconstantin.wordpress.com/2019/02/25/humans-who-are-not-concentrating-are-not-general-intelligences/) can easily distinguish Green partisans from truthseekers, but the [social-punishment machinery](http://benjaminrosshoffman.com/blame-games/) can't process more than [five words at a time](https://www.lesswrong.com/posts/4ZvJab25tDebB8FGE/you-have-about-five-words)

everyone knows

if one side has all the brains

https://www.lesswrong.com/rationality/how-much-evidence-does-it-take

"Tails Risk"

the meta-hill is a Schelling point for dying on

[The Correct Contrarian Cluster](https://www.lesswrong.com/posts/9KvefburLia7ptEE3/the-correct-contrarian-cluster)