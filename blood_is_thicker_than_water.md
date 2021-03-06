# Blood Is Thicker Than Water 🐬

**Followup to**: [Where to Draw the Boundaries?](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries)

_Without denying the obvious similarities that motivated the initial categorization `{salmon, guppies, sharks, dolphins, trout, ...}`, there is_ more structure _in the world: to maximize the probability your world-model assigns to your observations of dolphins, you need to take into consideration the many aspects of reality in which the grouping `{monkeys, squirrels, dolphins, horses ...}` makes more sense._

_The old category might have been "good enough" for the purposes of the sailors of yore, but as humanity has learned more, as our model of Thingspace has expanded with more dimensions and more details, we can see the ways in which the original map failed to carve reality at the joints ..._

So the one comes to you—a-_gain_—and says:

> Hold on. _In what sense_ did the original map fail to carve reality at the joints? You don't deny the obvious similarities between dolphins and fish—between dolphins and _other_ fish. That's a [cluster in configuration space](https://www.lesswrong.com/posts/WBw8dDkAWohFjWQSk/the-cluster-structure-of-thingspace)! The observation that dolphins are evolutionarily related to mammals may be an interesting fact that specialized professional evolutionary biologists care about for some inscrutible specialist reason. But _I'm_ not a professional evolutionary biologist. Choosing to define categories around evolutionary relatedness rather than macroscopic human-relevant features seems like an arbitrary æsthetic whim. Why should _I_ care about phylogenetics, at all?

This one is going to take a few paragraphs.

Focusing on evolutionary relatedness is not an arbitrary æsthetic whim because evolution _actually happened_. Evolution isn't just a story that our Society's specialists happen to have chosen on æsthetic grounds; they chose it [_because it predicts what we see in the world_](https://en.wikipedia.org/wiki/Nothing_in_Biology_Makes_Sense_Except_in_the_Light_of_Evolution). You _can't_ choose a substantively different theory and make the same predictions about the real world. (At most, you'd end up with an isomorphic theory with additional [epiphenominal](https://www.lesswrong.com/posts/fdEWWr8St59bXLbQr/zombies-zombies) elements, asserting that an allele rose in frequency ["because" the angels willed it](https://www.lesswrong.com/posts/WqGCaRhib42dhKWRL/if-many-worlds-had-come-first), without an account of why the angels' will happens to line up with what would have transpired if there were no angels.) Similarly, category definitions [represent hidden probabilistic inferences](https://www.lesswrong.com/posts/3nxs2WYDGzJbzcLMp/words-as-hidden-inferences); [you _can't_ "redraw" the "boundaries" of the categories your mind actually uses and still make the same predictions about the real world](https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception). Accordingly, it shouldn't be surprising that our knowledge of evolution turns out to have implications for how we should categorize organisms—not as an æsthetic choice, but for deep structural _reasons_ that can be understood mechanistically.

One element of the evolutionary worldview is a "continuity" assumption: all else being equal, creatures that are more closely related are more similar _in general_. Creationists sometimes try to discredit evolution by ridiculing the absurdity of a monkey giving birth to a person. But actually, evolutionary biologists [_agree_ on the absurdity of that specific scenario](https://www.lesswrong.com/posts/4Bwr6s9dofvqPWakn/science-as-attire)! Monkeys _don't_ suddenly give birth to humans in a single generation. If they did, that would _utterly falsify_ our understanding of evolution! Rather, monkeys and humans had a common ancestor many generations back, with the separate lines of descent leading to present-day monkeys and present-day humans each accumulating their own differences one mutation at a time.

The fact that evolution persists information in the genome creates a regularity in the world that can be exploited by [cognitive algorithms](https://www.lesswrong.com/posts/HcCpvYLoSFP4iAqSz/rationality-appreciating-cognitive-algorithms) that know about phylogeny. In terms of [the formalization of causality with directed acyclic graphs](https://www.lesswrong.com/posts/hzuSDMx7pd2uxFc5w/causal-diagrams-and-causal-models) [pioneered by Judea Pearl and others](https://www.lesswrong.com/posts/jnjjzkH8Fdzg4D6EK/causality-a-chapter-by-chapter-review), an organism's genome is at the [root](https://en.wikipedia.org/wiki/Rooted_graph) of the causal graph underlying all other features of an organism:

![](https://i.imgur.com/7ksShzY.png)

Conditioning on the "dolphin DNA" node in the diagram [d-separates](http://bayes.cs.ucla.edu/BOOK-2K/d-sep.html) the paths between the "blowhole" and "flippers" nodes that run through the "dolphin DNA" node. That means that—assuming there aren't any other paths between "blowhole" and "flippers" that _don't_ go through "dolphin DNA"—"blowhole" and "flippers" become conditionally independent given "dolphin DNA": when I see a creature with a blowhole, that makes me more likely to think it's a dolphin, which makes me more likely to think it has flippers, but given that I know something is a dolphin, learning more about its flippers doesn't change my predictions about its blowhole.

But [conditional independence assertions of this kind are _exactly_ what makes "categorizing" a useful AI technique in the first place](https://www.lesswrong.com/posts/gDWvLicHhcMfGmwaK/conditional-independence-and-naive-bayes). It's often helpful to visualize this by claiming that entities in the same category belong to a cluster in some configuration space, but this handy visual metaphor is lacking in rigor and well-definedness.

_What_ space? What do the dimensions of this space represent? ["Features"](https://en.wikipedia.org/wiki/Feature_(machine_learning))? But there are no pre-existing "features" in the world. Assuming the existence of a "space" up front is punting on most of the actual AI challenge. "There's conditional independence structure in the causal graph" is a meaningfully _deeper_ explanation than "There's a cluster in configuration space", because conditional independence is what what makes it possible to _construct_ a "space" _such that_ there are clusters. (Though this isn't a _complete_ explanation: we still need to figure out [where the "variables" in the causal graph come from](https://www.lesswrong.com/posts/6t9F5cS3JjtSspbAZ/finite-factored-sets-lw-transcript-with-running-commentary).)

Going beyond the configuration space metaphor is important because it lets us understand how we can _learn new things about dolphins that we don't already know_. Dolphins are complicated! Dolphins are complicated in a _very specific_ way. [Complex functional adaptations are universal within a species](https://www.lesswrong.com/posts/Cyj6wQLW6SeF6aGLy/the-psychological-unity-of-humankind) because [each individual part has to reach fixation before there can be selection pressure for the next incremental improvement](https://www.lesswrong.com/posts/ZyNak8F6WXjuEbWWc/the-wonder-of-evolution). That's why it's possible to claim that there are 206 bones in "the" human skeleton, even if most humans haven't had their bones counted. I haven't been able to find a citation on how many bones dolphins have, but I'm confident that it's the _same_ number for all or nearly-all members of a particular dolphin species.

But "number of bones" _wasn't_ one of the dimensions of the "space" that we originally noticed the dolphin cluster in! That's what the "carving reality at the joints" metaphor means: genetic relatedness is an underlying _generator_ of similarities, that _includes_ the "finned swimmy animals" properties that dolphins and fish have in common, but also includes many more [high-dimensional](https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1) details: how dolphins are warm-blooded, the way female dolphins nurse their live-born young, the way dolphins [sleep with only half their brain at a time](https://en.wikipedia.org/wiki/Unihemispheric_slow-wave_sleep), the specific bones in the (the!) dolphin skeleton (however many there turn out to be), the way dolphins [swim in a circle to trick fish into jumping and being eaten](https://en.wikipedia.org/wiki/Mud_ring_feeding), _&c._.

In contrast, "finned swimmy animals" is an intrinsically less cohesive subject matter: there _are_ similarities between them due to convergent evolution to the acquatic habitat, and it makes sense to want a [reasonably short word or phrase](https://www.lesswrong.com/posts/soQX8yXLbKy7cFvy8/entropy-and-short-codes) to describe those similarities in contexts where _only_ those similarities are relevant.

But that category "falls apart" very quickly as you consider more and more aspects of the creatures: the finned-swimmy-animals-with-gills are _systematically_ different from the finned-swimmy-animals-with-a-blowhole, in [_more_ ways](https://www.lesswrong.com/posts/yLcuygFfMfrfK8KjF/mutual-information-and-density-in-thingspace) than just the "respiratory organ" feature that I'm using in this sentence to _point to_ the two groups. 

A "definition" is just a description that helps someone else pick out "the same" category in their _own_ world-model: you can't pack everything there is to know about dolphins into the _definition_ of the word dolphin, for one reason because we don't _know_ everything there is to know about dolphins as an empirical regularity in the real world. The "finned swimmy animals" category [is "wrong"](https://www.lesswrong.com/posts/FaJaCgqBKphrDzDSj/37-ways-that-words-can-be-wrong) to the extent that [it fails to compress more information than is contained in its definition](https://www.lesswrong.com/posts/i2dfY65JciebF3CAo/empty-labels). The similarities induced by shared blood are a thicker subspace of configuration space than the similarities induced by living in the water.

The one replies:

> Okay, you've convinced me that phylogeny is of more than just specialist interest. But "fish" are a [paraphyletic](https://en.wikipedia.org/wiki/Paraphyly)


If you _are_ going to define categories based on phylogeny, 


[You know what else are paraphyletic taxa?](https://en.wikipedia.org/wiki/Paraphyly#Non-exhaustive_list_of_paraphyletic_groups) Monkeys (excludes apes, even though the common ancestor of monkeys and apes was a monkey). Reptiles (excludes birds, even though the common ancestor of birds was a reptile). Protists (excludes animals, plants, and fungi, even though their common ancestor would have been a protist). _Prokaryotes_ (excludes eukaryotes, even though the common ancestor of eukaryotes would have been a prokaryote).

[polyphyletic](https://en.wikipedia.org/wiki/Polyphyly)! That's even worse!


[...] only possible if you _stop playing nitwit games and admit that dolphins don't belong on the fish list_.

_(Thanks to [Tailcalled](https://www.lesswrong.com/users/tailcalled) for the "root of the causal graph" observation and [John S. Wentworth](https://www.lesswrong.com/users/johnswentworth) for explaining the importance of conditional independence.)_

-----


OUTLINE—

* Objection: you agree that the convergently-evolved similarities _exist_; in what sense is dolphins-are-fish _wrong_? Why should I care about phylogenetics, at all?
* Reply: Definitions are just a pointer to help you find the cluster, root of the causal graph, conditional independence
* Objection: But, but, if you are using phylogenetics as your criterion, why paraphyly?
* Reply: We at least want a connected set on phylogenetic space, but we're not just looking at an unlabeled tree; it makes sense to split off groups that diverged, many examples, bats, penguins; we expect fish/mammal/reptile/bird to be mutually exclusive
* dark skinned Indians aren'te black
* Objection: but then shouldn't we pick different words for the convergent and phylo clusters? Uncomfortable with wavering lines around "berry"
* Reply: story for how we end up with multiple senses attached to the same word


I don't personally notice the difference between alligators and crocodiles, but precisely because I don't need to care, you don't see me demanding a hypernym

Aristotle argued that they were mammals!!
https://en.wikipedia.org/wiki/Cetology 

----

As part of [a review of a book on post-traumatic stress disorder](https://slatestarcodex.com/2019/11/12/book-review-the-body-keeps-the-score/), psychiatrist Scott Alexander casually mentions the American Psychiatric Association's "philosophical commitment to categorizing by symptoms rather than cause": "[w]hen the APA decides not to [recognize developmental trauma disorder], they're not necessarily rejecting the seriousness of child abuse, only saying it's not the kind of thing they build their categories around."

In a sane world, this would be _utterly discrediting_ to the APA. The cognitive function of categories is to group relevantly similar things together in order to make similar predictions and decisions about them. But in order to treat a condition, causes are of supreme relevance! Medical doctors understand this: we consider bacterial and viral infections to be different categories of disease even when they cause similar symptoms, because antibiotics can treat the former but not the latter. No matter what words are used to describe it, at some point your decision algorithm _needs_ to categorize by cause _in order to compute the correct treatment_. If the authoritative body of professional psychiatrists has a "philosophical committment" against this, that means _we don't have a science of psychiatry_.

-----

https://www.lesswrong.com/posts/4Bwr6s9dofvqPWakn/science-as-attire

https://www.lesswrong.com/posts/jAToJHtg39AMTAuJo/evolutions-are-stupid-but-work-anyway

-----

If you live in human civilization and don't really _need_ to carve up the life forms around you in much detail—if your use-case for thinking about acquatic animals is _watching a nature documentary_ (for entertainment??) rather than living and working with them every day, then you might think the deeper causal structure isn't buying you anything, but I think you would change your mind if you were a veternarian or a zoologist who actually had skin in the game in describing this part of the world.

When people have skin in the game, they care about the underlying mechanisms and want short codewords for them. If you hurt your ankle while running, you would probably be interested to _know_ whether it was a [sprain or a stress fracture](https://ercare24.com/difference-sprain-vs-fracture/) because that affects your decisions about how to recover. You wouldn't say, "Well, all I know is that my ankle hurts—that's all a child would know—so I'm going to call it a _hurtankle_; I don't care about anatomy."

Phylogenetics is also a lot more _objective_: it's easier to [stabilize a _shared_ map](https://www.lesswrong.com/posts/edEXi4SpkXfvaX42j/schelling-categories-and-simple-membership-tests) on the facts of evolutionary history (which we can all agree on in the limit of good science) then the vagaries of what I personally think tastes good on pizza.

And this subjectivity also applies to animal classification. Some might be inclined to argue "bats are birds" (flappy flying animals) on the same grounds as "dolphins are fish" (flappy swimmy animals). But did you know the German word for bat is [_Fledermaus_](https://en.wiktionary.org/wiki/Fledermaus) ("flutter mouse"), which dates back to _fledarmūs_ in [Old High German](https://en.wikipedia.org/wiki/Old_High_German)? Apparently, people way back in the tenth century or so (long before evolution was understood) already thought bats were like a mammal-that-happened-to-fly rather than a bird-that-happened-to-be-furry.
