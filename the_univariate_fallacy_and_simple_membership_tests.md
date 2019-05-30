# The Univariate Fallacy, and Simple Membership Tests

**Followup to**: [Where to Draw the Boundaries?](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries)

_Or there might be social or psychological forces anchoring word usages on identifiable Schelling points that are easy for different people to agree upon, even at the cost of some statistical "fit"_ ...

The one comes to you and says, "That part about Schelling points sounded interesting. What did you mean by that? Can you give an example?"

Sure. So there's this statistical phenomenon sometimes called the "univariate fallacy", where it's possible for two multivariate distributions to overlap along in any one variable, but be cleanly separable when you look at the entire [configuration space](https://www.lesswrong.com/posts/WBw8dDkAWohFjWQSk/the-cluster-structure-of-thingspace) at once. This is perhaps easiest to see with an illustrative diagram—

[TODO: diagram]

(Eliezer Yudkowsky [proposes "covariance denial fallacy" or "cluster erasure fallacy"](https://twitter.com/ESYudkowsky/status/1124757043997372416) as potential alternative names.)

Imagine we have two clusters of datapoints in {1, 2, 3, 4}¹⁰⁰, call them A and B; suppose that for every _x_\__i_ for _i_ from 1 to 100, points in the A cluster have the following distribution: [1/4, 7/16, 1/4, 1/16] and points from the B cluster have this distribution [1/16, 1/4, 7/16, 1/4].

[TODO: phrase this clearer]

[TODO: use "typical set" reasoning to show that these are distinct clusters
https://en.wikipedia.org/wiki/Asymptotic_equipartition_property
http://zackmdavis.net/blog/2019/05/the-typical-set/
]

(I originally imagined this with normal distributions with different means, but choosing a discrete distribution makes explicit calculations easier, and it doesn't matter for the point I'm trying to make.)

From the standpoint of ["the way to carve reality at its joints, is to draw your boundaries around concentrations of unusually high probability density in Thingspace"](https://www.lesswrong.com/posts/yLcuygFfMfrfK8KjF/mutual-information-and-density-in-thingspace), the correct categorization is clear: we have two distinct clusters, so we should draw a category boundary around each cluster. What could possibly change this moral?

Well, one thing to notice here is that the predictive work we out of category-membership is spread out across _many_ variables. Observing that one of the variables from one of the datapoints takes the value 2 gives you a 7/4 (= 1.75) likelihood ratio (or probability 0.63) in favor of that datapoint coming from cluster A rather than cluster B, or lg(7/4) ≈ 0.807 bits of evidence.

That's ... not a whole lot of evidence. If guessed that the datapoint came from cluster A based on that much evidence, you'll be wrong about 4 times out of 10. It's only by looking at _many_ variables that we can become confident about cluster-membership.

Suppose you needed to _coordinate_ with someone else to make decisions about these entities, but each of you only get to observe a couple of coordinates from each point.



[Leaky Generalizations](https://www.lesswrong.com/posts/Tc2H9KbKRjuDJ3WSS/leaky-generalizations)

Make sure to mention that clustering is hard—
http://alexhwilliams.info/itsneuronalblog/2015/09/11/clustering1/
http://alexhwilliams.info/itsneuronalblog/2015/10/01/clustering2/

Goodhart's Law: https://www.lesswrong.com/posts/EbFABnst8LsidYs5Y/goodhart-taxonomy regressional Goodhart

The one says, "No, I meant, like, a real-world example."

Oh. You're one of _those_ readers. Fine, consider—

Age of majority

Political party self-identification

Credentialism

connect to simaculra levels