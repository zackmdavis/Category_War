# Schelling Categories, and Simple Membership Tests

**Followup to**: [Where to Draw the Boundaries?](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries), [The Univariate Fallacy](https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy)

_Or there might be social or psychological forces anchoring word usages on identifiable Schelling points that are easy for different people to agree upon, even at the cost of some statistical "fit"_ ...

The one comes to you and says, "That paragraph about Schelling points sounded interesting. What did you mean by that? Can you give an example?"

Sure. Previously on _Less Wrong_, in ["The Univariate Fallacy"](https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy), we studied points sampled from two probability distributions




From the standpoint of ["the way to carve reality at its joints, is to draw your boundaries around concentrations of unusually high probability density in Thingspace"](https://www.lesswrong.com/posts/yLcuygFfMfrfK8KjF/mutual-information-and-density-in-thingspace), the correct categorization of our points is clear. We have two distinct clusters. The [conditional independence](https://www.lesswrong.com/posts/gDWvLicHhcMfGmwaK/conditional-independence-and-naive-bayes) criterion is satisfied: _given_ a point's cluster-membership, knowing one of the $x_i$ doesn't tell you anything about $x_j$ for _j_ ≠ _i_. So we should draw a category boundary around each cluster. What could possibly change this moral?

Well, suppose you needed to _coordinate_ with someone else to make decisions about these entities—that is, it's important not just that you and your partner make good decisions, but also that you make the _same_ decision—but that each of you only got to observe one or two random coordinates from each point. As we just saw, the predictive work we get from category-membership in this scenario is spread across _many_ variables: if you only get to observe a _few_ dimensions, you have a lot of uncertainty about cluster-membership (that is, uncertainty about the other dimensions that you haven't observed, but which affect the _ex post_ quality of your decision).

If you and your partner were both ideal Bayesian calculators who could communicate costlessly, you would [share your observations](https://www.overcomingbias.com/2009/02/share-likelihood-ratios-not-posterior-beliefs.html), work out the correct probability, and use that to make optimal decisions. But suppose you _couldn't_ do that—either because communication is expensive, or your partner was bad at math, or any other reason. Then it would be sad if you happened to see x₉ = 2 and said "It's an A (probably)!", and your partner happened to see x₂₇ = 3 and said "It's a B (I think)!", and the two of you made inconsistent decisions.

Okay, _now_ suppose that there's actually a forty-first, binary, variable that I didn't tell you about earlier, distributed like so:

$$P_A(x_41) = \begin{cases} 5/6 & x_41 = 0 \\ 1/6 & x_41 = 1 \\ \end{cases}$$

$$P_B(x_41) = \begin{cases} 1/6 & x_41 = 0 \\ 5/6 & x_41 = 1 \\ \end{cases}$$

Observing _x₄₁_ gives you log₂(5) ≈ 2.322 bits of evidence about cluster-membership, somewhat more than you can get from any one observation of one of the $x_i$ for _i_ ∈ {1...40}. [TODO: compare to min/max/avg evidence in the x1-40 case] If you and your partner can both observe _x₄₁_, you might end up wanting to base your shared categories and language on _that_, even at the 

Even if _x₄₁_ itself has no effect on the quality of your decisions, if it's something you can _agree_ on that _correlates_ with the things you care about, then in the 


Thanks for reading!

-------

The one says, "No, I meant, like, a _real world_ example about dolphins or something. Not some dumb math thing for nerds. What is this post _really_ about?"

Oh. One of _those_ readers, I see. Fine, I can probably think of something.

Ummmm ...

Okay, here's something, maybe. What's the deal the [age of majority](https://en.wikipedia.org/wiki/Age_of_majority)?

Society needs to decide who it wants to be allowed to vote, stand trial, sign contracts, serve in the military, _&c._ Whether it's a good idea for a particular person to have these privileges presumably depends on various _relevant_ features of that person: things like cognitive ability, foresight, wisdom, _&c_. In particular, it would be _pretty weird_ for someone's fitness to vote to directly depend on _how many times the Earth has gone around the sun since they were born_. What does _that_ number have to do with anything?

It doesn't! But if Society isn't well-coordinated enough to _agree_ on the exact prerequisites for voting and how to measure them, but _can_ agree that most twenty-five-year-olds have them and most eleven-year-olds don't, then we end up choosing some arbitrary age cutoff as the criterion for our "legal adulthood" social construct. It _works_, but it's just a legal fiction—and not necessarily a particularly good fiction, as any bright teenagers reading this can attest.

If I told you that a particular fourteen-year-old was very "mature", that's a meaningful statement—we have shared meaning attached to the word _mature_, such that my describing someone that way constrains your anticipations—but it's a _really complicated_ meaning.

http://benjaminrosshoffman.com/excerpts-from-a-larger-discussion-about-simulacra/
https://slatestarcodex.com/2016/04/04/the-ideology-is-not-the-movement/
https://www.lesswrong.com/posts/EbFABnst8LsidYs5Y/goodhart-taxonomy

Or consider political party self-identification.

Credentialism

connect to simaculra levels
