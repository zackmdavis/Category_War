# The Univariate Fallacy, and Simple Membership Tests

**Followup to**: [Where to Draw the Boundaries?](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries)

_Or there might be social or psychological forces anchoring word usages on identifiable Schelling points that are easy for different people to agree upon, even at the cost of some statistical "fit"_ ...

The one comes to you and says, "That paragraph about Schelling points sounded interesting. What did you mean by that? Can you give an example?"

Sure. So there's this statistical phenomenon sometimes called the "univariate fallacy", where it's possible for two multivariate distributions to overlap along in any one variable, but be cleanly separable when you look at the entire [configuration space](https://www.lesswrong.com/posts/WBw8dDkAWohFjWQSk/the-cluster-structure-of-thingspace) at once. This is perhaps easiest to see with an illustrative diagram—

[diagram here]

(Eliezer Yudkowsky [proposes "covariance denial fallacy" or "cluster erasure fallacy"](https://twitter.com/ESYudkowsky/status/1124757043997372416) as potential alternative names.)

Let's make this more concrete. Imagine we have some datapoints that live in the forty-dimensional space {1, 2, 3, 4}⁴⁰ that are sampled from one of two probability distibutions, which we'll call $P_A$ and $P_B$.

For simplicity, let's suppose that the individual variables _x₁_, _x₂_, ... _x₄₀_—the coördinates of a point in our forty-dimensional space—are statistically independent. For every individual $x_i$, the marginal distribution of $P_A$ is—

$$P_A(x_i) = \begin{cases} 1/4 & x_i = 1 \\ 7/16 & x_i = 2 \\ 1/4 & x_i = 3 \\ 1/16 & x_i = 4 \\ \end{cases}$$

And for $P_B$—

$$P_B(x_i) = \begin{cases} 1/16 & x_i = 1 \\ 1/4 & x_i = 2 \\ 7/16 & x_i = 3 \\ 1/4 & x_i = 4 \\ \end{cases}$$

If you look at any one particular $x_i$-coördinate for a point, you can't be confident which distribution the point was sampled from. For example, seeing that x₁ takes the value 2 gives you a 7/4 (= 1.75) likelihood ratio (or probability ~0.64) in favor of that the point having been sampled from $P_A$ rather than $P_B$, which is log₂(7/4) ≈ 0.807 bits of evidence.

That's ... not a whole lot of evidence. If you guessed that the datapoint came from $P_A$ based on that much evidence, you'd be wrong about 4 times out of 10.

And yet if we look at _many_ variables, we can achieve _supreme, godlike_ confidence about which distribution a point is from. _Proving_ this is left as an exercise to the particularly intrepid reader, but a concrete _demonstration_ is probably simpler and should be pretty convincing. Let's write some Python code to sample a point **x⃗** ∈ {1, 2, 3, 4}⁴⁰ sampled from $P_A$—

```
import random

def a():
    return random.sample([1]*4 + [2]*7 + [3]*4 + [4], 1)[0]

x = [a() for _ in range(40)]
print(x)
```

Go ahead and [run the code yourself](https://repl.it/languages/python3). You'll _probably_ get a value of `x` that "looks something like"

```
[1, 3, 1, 3, 2, 2, 3, 4, 3, 2, 2, 1, 3, 2, 2, 2, 1, 1, 2, 4, 1, 3, 1, 2, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1]
```

Because the coördinates/variables are statistically independent, tallying up (multiplying) the individual likelihood ratios from each variable to calculate our posterior probability that the point was sampled from $P_A$ (as opposed to $P_B$) is only a little bit more code.

[TODO: clarify "posterior probability" wording, we _know_ where we did in fact sample this point from]

```
import logging

logging.basicConfig(level=logging.INFO)

def odds_to_probability(o):
    return o/(1+o)

def tally_likelihoods(x, p_a, p_b):
    total_odds = 1
    for i, x_i in enumerate(x, start=1):
        lr = p_a[x_i-1]/p_b[x_i-1]
        logging.info("x_%s = %s, likelihood ratio is %s", i, x_i, lr)
        total_odds *= lr
    return total_odds

print(
    odds_to_probability(
        tally_likelihoods(
            x,
            [1/4, 7/16, 1/4, 1/16],
            [1/16, 1/4, 7/16, 1/4]
        )
    )
)
```

You'll _probably_ see something like this—

```
INFO:root:x_1 = 1, likelihood ratio is 4.0
INFO:root:x_2 = 3, likelihood ratio is 0.5714285714285714
INFO:root:x_3 = 1, likelihood ratio is 4.0
[blah blah, redacting some lines to save vertical space in the blog post, blah blah]
INFO:root:x_37 = 1, likelihood ratio is 4.0
INFO:root:x_38 = 2, likelihood ratio is 1.75
INFO:root:x_39 = 2, likelihood ratio is 1.75
INFO:root:x_40 = 1, likelihood ratio is 4.0
0.9999999998348625
```

That's pretty confident!

From the standpoint of ["the way to carve reality at its joints, is to draw your boundaries around concentrations of unusually high probability density in Thingspace"](https://www.lesswrong.com/posts/yLcuygFfMfrfK8KjF/mutual-information-and-density-in-thingspace), the correct categorization of our points is clear. We have two distinct clusters. The [conditional independence](https://www.lesswrong.com/posts/gDWvLicHhcMfGmwaK/conditional-independence-and-naive-bayes) criterion is satisfied: _given_ a point's cluster-membership, knowing one of the $x_i$ doesn't tell you anything about $x_j$ for _j_ ≠ _i_. So we should draw a category boundary around each cluster. What could possibly change this moral?

Well, suppose you needed to _coordinate_ with someone else to make decisions about these entities—that is, it's important not just that you and your partner make good decisions, but also that you make the _same_ decision—but that each of you only got to observe one or two random coordinates from each point. As we just saw, the predictive work we get from category-membership in this scenario is spread across _many_ variables: if you only get to observe a _few_ dimensions, you have a lot of uncertainty about cluster-membership (that is, uncertainty about the other dimensions that you haven't observed, but which affect the _ex post_ quality of your decision).

If you and your partner were both ideal Bayesian calculators who could communicate costlessly, you would [share your observations](https://www.overcomingbias.com/2009/02/share-likelihood-ratios-not-posterior-beliefs.html), work out the correct probability, and use that to make optimal decisions. But suppose you _couldn't_ do that—either because communication is expensive, or your partner was bad at math, or any other reason. Then it would be sad if you happened to see x₉ = 2 and said "It's an A (probably)!", and your partner happened to see x₂₇ = 3 and said "It's a B (I think)!", and the two of you made inconsistent decisions.

Okay, _now_ suppose that there's actually a forty-first, binary, variable that I didn't tell you about earlier, distributed like so:

$$P_A(x_41) = \begin{cases} 5/6 & x_41 = 0 \\ 1/6 & x_41 = 1 \\ \end{cases}$$

$$P_B(x_41) = \begin{cases} 1/6 & x_41 = 0 \\ 5/6 & x_41 = 1 \\ \end{cases}$$

Observing _x₄₁_ gives you log₂(5) ≈ 2.322 bits of evidence about cluster-membership, somewhat more than you can get from any one observation of one of the $x_i$ for _i_ ∈ {1...40}. [TODO: compare to min/max/avg evidence in the x1-40 case] If you and your partner can both observe _x₄₁_, you might end up wanting to base your shared categories and language on _that_, even at the 

Even if _x₄₁_ itself has no effect on the quality of your decisions, if it's something you can _agree_ on that _correlates_ with the things you care about, then in the 

In conclusion, this example illustrates how 

Thanks for reading!

-------

The one says, "No, I meant, like, a real-world example. Like, not some dumb math thing for nerds, but a _real-world takeaway_ about, like, whether I should support the [Blues or Greens](https://www.lesswrong.com/posts/6hfGNLf4Hg5DXqJCF/a-fable-of-science-and-politics) in the next chariot race. Or _at least_ something about dolphins. What is this post _really_ about?"

It's about ... math? Or like, the relationship between math and human natural language? I mean, I know I have lot of room to improve as a writer, but I don't think I was _that_ unclear, so I'm puzzled why—

"You can't expect me to believe that. [Contextualizing norms](https://www.lesswrong.com/posts/7cAsBPGh98pGyrhz9/decoupling-vs-contextualising-norms) are valid rationality norms. C'mon, what's your _real_ agenda here, huh?"

Oh. One of _those_ readers, I see. _Fine_, alright, I can probably think of something.

Ummmm ...

Let's see ...

Oh, here's something, maybe. What's the deal the [age of majority](https://en.wikipedia.org/wiki/Age_of_majority)?

Society needs to decide who it wants to be allowed to vote, stand trial, sign contracts, serve in the military, _&c._ Whether it's a good idea for a particular person to have these privileges presumably depends on various _relevant_ features of that person: things like cognitive ability, foresight, wisdom, _&c_. In particular, it would be _pretty weird_ for someone's fitness to vote to directly depend on _how many times the Earth has gone around the sun since they were born_. What does _that_ number have to do with anything?

It doesn't! But if Society isn't well-coordinated enough to _agree_ on the exact prerequisites for voting and how to measure them, but _can_ agree that most twenty-five-year-olds have them and most eleven-year-olds don't, then we end up choosing some arbitrary age cutoff as the criterion for our "legal adulthood" social construct. It _works_, but it's just a legal fiction—and not necessarily a particularly good fiction, as any bright teenagers reading this can attest.

If I told you that a particular fourteen-year-old was very "mature", that's a meaningful statement—we have shared meaning attached to the word _mature_, such that my describing someone that way constrains your anticipations—but it's a _really complicated_ meaning.



Or consider political party self-identification.

Credentialism

connect to simaculra levels
