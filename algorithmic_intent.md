## Algorithmic Intent: A Hansonian Generalized Anti-Zombie Principle

> "Why didn't you tell him the truth? Were you afraid?"

> "I'm not _afraid_. I _chose_ not to tell him, because I anticipated negative consequences if I did so."

> "What do you think 'fear' _is_, exactly?"

It's tempting to think that consciousness isn't part of the physical universe. Seemingly, we can imagine a world _physically_ identically to our own—the same atom-configurations evolving under the same laws of physics—but with no _consciousness_, a world inhabited by [philosophical "zombies"](https://www.lesswrong.com/posts/fdEWWr8St59bXLbQr/zombies-zombies) who move and talk, but only as mere automatons, without the spark of _mind_ within.

It can't actually work that way. When we _talk_ about consciousness, we do so with our merely physical lips or merely physical keyboards. The causal explanation for talk about consciousness has to _either_ exist entirely within physics (in which case anything we say about consciousness is causally unrelated to consciousness, which is absurd), _or_ there needs to be some place where the laws of physics are violated as the immaterial soul is observed to be "tugging" on the brain (which is in-principle experimentally detectible). Zombies can't exist.

But if consciousness exists within physics, it should respect a certain ["locality"](https://www.lesswrong.com/posts/XDkeuJTFjM9Y2x6v6/which-basis-is-more-fundamental), a [Generalized Anti-Zombie Principle](https://www.lesswrong.com/posts/kYAuNJX2ecH2uFqZ9/the-generalized-anti-zombie-principle): if the configuration-of-matter that _is you_, is conscious, then _almost_-identical configurations should also be conscious for _almost_ the same reasons. An artificial neuron that implements the same input-output relationships as a biological one, would "play the same role" within the brain, which would continue to compute the same externally-observable behavior.

We don't want to push the Generalized Anti-Zombie Principle so far as to say that only externally-observable behavior matters and internal mechanisms don't matter at all, because substantively different internal mechanisms could compute the same behavior. Prosaically, [acting](https://en.wikipedia.org/wiki/Acting) exists: even the best method actors aren't really occupying the same mental state that the characters they portray would be in. In the limit, we could (pretend that we could) imagine [an incomprehensibly vast Giant Lookup Table](https://www.lesswrong.com/posts/k6EPphHiBH4WWYFCj/gazp-vs-glut) that has stored the outputs that a conscious mind would have produced in response to any input. Is such a Giant Lookup Table—an entirely static mapping of inputs to outputs—conscious? Really?

But this thought experiment requires us to posit the existence of a Giant Lookup Table that _just happens_ to mimic the behavior of a conscious mind. _Why_ would that happpen? Why would that _actually_ happen, in the real world? (Or the closest possibly-impossible possible world large enough to contain the Giant Lookup Table.) "Just assume it happened by coincidence, for the sake of the thought experiment" is unsatisfying, because that kind of arbitrary [thermodynamic](https://www.lesswrong.com/posts/QkX2bAkwG2EpGvNug/the-second-law-of-thermodynamics-and-engines-of-cognition) miracle doesn't help us understand what kind of cognitive work the ordinary [simple concept](https://www.lesswrong.com/posts/82eMd5KLiJ5Z6rTrr/superexponential-conceptspace-and-simple-words) of _consciousness_ is doing for us. You can _assume_ that a broken and scrambled egg will spontaneously reassemble itself for the sake of a thought experiment, but the interpretation of your thought-experimental results may seem tendentious given that we have Godlike confidence that [you will never, ever see that happen in the real world](https://www.lesswrong.com/posts/zFuCxbY9E2E8HTbfZ/perpetual-motion-beliefs).

The [_hard_ problem of consciousness](http://www.scholarpedia.org/article/Hard_problem_of_consciousness) is still confusing unto me—it [_seems_ impossible](https://www.lesswrong.com/posts/XzrqkhfwtiSDgKoAF/wrong-questions) that any arrangement of mere matter could add up to the ineffable _qualia_ of subjective experience. But the easier and yet clearly _somehow_ related problem of how mere matter can do information-processing—can do things like construct "models" by [using sensory data to correlate its internal state with the state of the world](https://www.lesswrong.com/posts/6s3xABaXKPdFwA3FS/what-is-evidence)—seems understanable, and a lot of our ordinary _use_ of the concept of _consciousness_ necessarily deals with the easy problems of perception and [interpreting people's self-reports](https://en.wikipedia.org/wiki/Heterophenomenology), even if we [can't _see_ the identity](https://www.lesswrong.com/posts/KmghfjH6RgXvoKruJ/hand-vs-fingers) between the easy problems and the hard problem. If I were to punch you in the face, I can predict that you'd react somehow—perhaps by saying, "Ow, that really hurt! I'm perceiving an ontologically-basic _quale_ of pain right now! I hereby commit to extract a costly revenge on you if you do that again, even at disproportionate cost to myself!" The fact that the human brain has the detailed functional structure to compute that _kind_ of response, whereas rocks and trees don't, is why we can be confident that [rocks and trees don't secretly have minds like ours](https://www.lesswrong.com/posts/f4RJtHBPvDRJcCTva/when-anthropomorphism-became-stupid).

So far, so standard. [(Read the Sequences!)](https://www.readthesequences.com/) My interest today is in exploring how well this style of argument applies to other concepts besides _consciousness_—seeking, perhaps, a Generalized Generalized Anti-Zombie Principle.

Consider the idea of _sorting_. Human alphabets aren't just a set of symbols—we also have a concept of the alphabet coming in some canonical _order_. The order of the alphabet doesn't play any role in the written language itself: you wouldn't have trouble reading books from an alternate world where the order of the Roman alphabet ran _KUWONSEZYFIJTABHQGPLCMVDXR_, but all English words were the same—but you would have trouble _finding_ the books on a shelf that wasn't sorted in the order you're used to. Sorting is useful because it lets us find things more easily: "The title I'm looking for starts with a _P_, but the book in front of me starts with a _B_; skip ahead" is faster than "look at every book until you find the one".

In the days before computers, the work of sorting was always done by humans: if you want your physical bookshelf to be alphabetized, you probably don't have a lot of other options than manually handling the books yourself ("This title starts with a _Pl_; I should put it ... da da da _here_, after this title starting with _Pe_ but before its neighbor starting with _Po_"). But the _computational work_ of sorting is simple enough that we can program computers to do it and _prove theorems_ about what is being accomplished, without getting confused about the sacred mystery of sorting-ness.

Very different systems can perform the work of sorting, but whether it's a human tidying her bookshelf, or a [punchcard-sorting machine](https://en.wikipedia.org/wiki/IBM_card_sorter), or a modern computer sorting in RAM, it's useful to have a [short word](https://www.lesswrong.com/posts/soQX8yXLbKy7cFvy8/entropy-and-short-codes) to describe _processes_ that "take in" some list of inputs, and "output" a list with the same elements ordered with respect to some criterion, for which we can know that the theorems we prove about sorting-in-general will apply to any system that implements sorting. (For example, sorting processes that can [only compare two items to check which is "greater"](https://en.wikipedia.org/wiki/Comparison_sort) (as opposed to being able to [exploit more detailed prior information about the distribution of elements](https://en.wikipedia.org/wiki/Sorting_algorithm#Non-comparison_sorts)) can expect to have to perform $n \log n$ comparisons, where $n$ is the length of the list.)

Someone who wasn't familiar with computers might refuse to recognize sorting algorithms as _real_ sorting, as opposed to mere ["artificial sorting"](https://www.lesswrong.com/posts/YhgjmCxcQXixStWMC/artificial-addition). After all, a human sorting her bookshelf _intends_ to put the books in order, whereas the computer is just an automaton following instructions, and doesn't intend anything at all—a zombie sorter!

But this position is kind of silly, a [gerrymandered concept definition](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries). To be sure, it's true that the internal workings of the human are _very_ different from that of the computer. The human wasn't special-purpose programmed to sort and is necessarily doing a lot _more_ things: the subjective experience of eagerly looking forward to how much easier it will be to find things after the bookshelf is sorted, has no analogue inside the computer. But that subjective experience isn't particularly relevant to the _work of sorting_, both the human and computer have to be doing the same _kind_ of operations. The exact sequence of comparisons performed can differ, as it would between a computer program implementing [quicksort](https://en.wikipedia.org/wiki/Quicksort) and another implementing [merge sort](https://en.wikipedia.org/wiki/Merge_sort), but the comparisons—the act of taking two elements, two books, and placing them somewhere that _depends_ on which one is "greater", needs to happen _in order to get the right answer_.

The concept of "sorting into alphabetical order" may have been invented before our concept of "computers", but the most natural concept of sorting—the one that [carves reality at the joints](https://www.lesswrong.com/posts/d5NyJ2Lf6N22AD9PB/where-to-draw-the-boundary)—includes computers performing quicksort, mergesort, _&c._., despite the lack of conscious "intent."











http://zackmdavis.net/blog/2012/07/an-idea-for-a-psychology-experiment/


[sorting algorithm]

[expand the generalized principle beyond "consciousness", to "intent": "consciousness" makes preidctions about heterophenomenological behavior, "intent" also makes predictions about behavior]

[false faces]

> "Accuse me of _fraud_? How _dare_ you?! Sure, I'm not a perfect person free from all bias, but—"

> "Bias. Is that your word for having a disposition to communicate in a way that causes others to make incorrect predictions about the value you have to offer, in a direction that moves resources towards you?"

> "Uh. I guess you could say that."

> "What do you think 'fraud' _is_, exactly?"

[follow the improbability]

[optimization—when you can predict something better by observing the outcome rather than the mechanisms]

[conscious and unconscious fraud are different—but another agent who's dealing with you may wish to regard this as the difference between mergesort and quicksort]

https://www.lesswrong.com/posts/28bAMAxhoX3bwbAKC/are-your-enemies-innately-evil

https://www.lesswrong.com/posts/N9oKuQKuf7yvCCtfq/can-crimes-be-discussed-literally

https://sideways-view.com/2016/11/26/if-you-cant-lie-to-others-you-must-lie-to-yourself/


"The bureaucrat, police officer, teacher, judge, or cable television company representative functions as [...], not as a co-modeling and fully interacting person. His behaviors are governed by top-down rules and scripts, with human discretion eliminated as much as possible."

(Sarah Perry, "The Essence of Peopling")
