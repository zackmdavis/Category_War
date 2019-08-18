# Schelling Categories, and Simple Membership Tests

**Followup to**: [Where to Draw the Boundaries?](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries)

_Or there might be social or psychological forces anchoring word usages on identifiable Schelling points that are easy for different people to agree upon, even at the cost of some statistical "fit"_ ...

The one comes to you and says, "That paragraph about Schelling points sounded interesting. What did you mean by that? Can you give an example?"

Sure. Previously on _Less Wrong_, in ["The Univariate Fallacy"](https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy), we studied points sampled from two multivariate probability distributions $P_A$ and $P_B$, and showed that it was possible to infer with very high probability which distribution a given point was sampled from, despite significant overlap in the marginal distributions for any one variable considered individually.

From the standpoint of ["the way to carve reality at its joints, is to draw your boundaries around concentrations of unusually high probability density in Thingspace"](https://www.lesswrong.com/posts/yLcuygFfMfrfK8KjF/mutual-information-and-density-in-thingspace), the correct categorization of the points in that example is clear. We have two clearly distinguishable clusters. The [conditional independence](https://www.lesswrong.com/posts/gDWvLicHhcMfGmwaK/conditional-independence-and-naive-bayes) property is satisfied: _given_ a point's cluster-membership, knowing one of the $x_i$ doesn't tell you anything about $x_j$ for _j_ ≠ _i_. So we should draw a category boundary around each cluster. Obviously. What could _possibly_ change this moral?

More constraints on the problem, that's what!

Suppose you needed to _coordinate_ with someone else to make decisions about these points—that is, it's important not just that you and your partner make good decisions, but also [that you make the _same_ decision](https://www.lesswrong.com/posts/9QxnfMYccz9QRgZ5z/the-costly-coordination-mechanism-of-common-knowledge#Coordination_Problems)—but that each of you only got to observe one coordinate from each point. As we saw, the predictive work we get from category-membership in this scenario is spread across _many_ variables: if you only get to observe a _few_ dimensions, you have a lot of uncertainty about cluster-membership (that is, uncertainty about the other dimensions that you haven't observed, but which affect the _ex post_ quality of your decision).

If you and your partner were both ideal Bayesian calculators who could communicate costlessly, you would [share your observations](https://www.overcomingbias.com/2009/02/share-likelihood-ratios-not-posterior-beliefs.html), work out the correct probability, and use that to make optimal decisions. But suppose you _couldn't_ do that—either because communication is expensive, or your partner was bad at math, or any other reason. Then it would be sad if you happened to see $x_9$ = 2 and said "It's an A (probably)!", and your partner happened to see $x_27$ = 3 and said "It's a B (I think)!", and the two of you made inconsistent decisions.

Okay, _now_ suppose that there's actually a forty-first, binary, variable that I didn't tell you about earlier, distributed like so:

$$P_A(x_41) = \begin{cases} 3/4 & x_41 = 0 \\ 1/4 & x_41 = 1 \\ \end{cases}$$

$$P_B(x_41) = \begin{cases} 1/4 & x_41 = 0 \\ 3/4 & x_41 = 1 \\ \end{cases}$$

Observing $x_41$ gives you $\log_2 3$ ≈ 1.585 bits of evidence about cluster-membership, which is more than the

$$\frac{1/4 + 1/16}{2} * |\log_2(4)| + \frac{7/16 + 1/4}{2} * |\log_2(7/4)| + \frac{1/4 + 7/16}{2} * |\log_2(4/7)| + \frac{1/16 + 1/4}{2} * |\log_2(4)|$$

≈ 1.18 bits you can get from any one observation of one of the $x_i$ for _i_ ∈ {1...40}.

If you and your partner can both observe $x_41$, you might end up wanting to base your shared categories and language on _that_—calling a point an "A" if it has $x_41$ = 0, even though such points actually came from $P_B$ a full quarter of the time—even if $x_41$ itself has no effect on the quality of your decisions, and what you _actually_ care about is wholely determined by the values of $x_1$ through $x_40$! It's not the [intension](https://www.lesswrong.com/posts/HsznWM9A7NiuGsp28/extensions-and-intensions) you would pick if you could make (and share) _more observations_—but _ex hypothesi_, you can't.

If you and your partner only get to observe one variable, $x_41$ is your best choice—the single variable that gives you the most information about the "natural" cluster-membership. That also makes it a [_Schelling point_](https://www.lesswrong.com/posts/yJfBzcDL9fBHJfZ6P/nash-equilibria-and-schelling-points)—if you and your partner didn't get to commmunicate in advance about how you want to draw your shared category boundaries, you could pick $x_41$ as your defining observation and be pretty confident your partner would make the same choice. We could imagine an even more pessimistic scenario in which the Schelling point category definition (a set of variables that "stuck out" from all the others) was _less_ predictive than some other candidates—but if you couldn't _coordinate_ to _pick_ one of the more predictive category systems, you might be stuck with the Schelling point.

In conclusion, the right categories to use _given_ constraints on communication and observation, might be different from the category boundaries you would draw from a "God's eye view", because consideration of which categories are easy for different agents to _coordinate_ on is also relevant, in addition to raw information-theoretic expressive power. Thus, "Schelling categories."

Thanks for reading!

-------

The one says, "No, I meant, like, a _real world_ example, not some dumb math thing for nerds. What is this post _really_ about?"

It's about ... math? Or like, the relationship between math and human natural language? Like, I was wondering what "second-order" caveats or complications there might be to the basic "carve reality at the joints" moral of our [standard Bayesian philosophy of language](https://www.lesswrong.com/posts/FaJaCgqBKphrDzDSj/37-ways-that-words-can-be-wrong), and some of my collaborators had been talking about the importanace of [_intersubjective_ epistemology](TODO: "humility argument for honesty" linky)—_shared_ mapmaking, so—

"But where's the _actionable takeaway_? Are you _hiding_ it? What's your _real_ agenda here, huh?"

Oh. One of _those_ readers, I see. Fine, I can probably think of some—how do you say?—"applications."

Ummmm ...

Let's see ...

Okay, here's something, maybe. What's the deal the [age of majority](https://en.wikipedia.org/wiki/Age_of_majority)?

Society needs to decide who it wants to be allowed to vote, stand trial, sign contracts, serve in the military, _&c._ Whether it's a good idea for a particular person to have these privileges presumably depends on various _relevant_ features of that person: things like cognitive ability, foresight, wisdom, relevant life experiences, _&c_. In particular, it would be _pretty weird_ for someone's fitness to vote to directly depend on _how many times the Earth has gone around the sun since they were born_. What does _that_ number have to do with anything?

It doesn't! But if Society isn't well-coordinated enough to _agree_ on the exact prerequisites for voting and how to measure them, but _can_ agree that most twenty-five-year-olds have them and most eleven-year-olds don't, then we end up choosing some arbitrary age cutoff as the criterion for our "legal adulthood" social construct. It _works_, but it's just a legal fiction—and not necessarily a particularly good fiction, as any bright teenagers reading this will doubtlessly attest.

If I told you that a particular fourteen-year-old was very "mature", that's a contentful statement: we have shared meaning attached to the word _mature_, such that my describing someone that way constrains your anticipations. But it's a _really complicated_ meaning, a statistical signal in behavior that your brain can pick up on, but which isn't particularly verifiable to others who might have reasons to doubt your character assessment. In contrast, age is easy for everyone to agree on. We could _imagine_ some hypothetical science-fictional Society that used brain scans and some sophisticated machine-learning classifer to determine which citizens get which privileges—but in our dumber, poorer world, calendars and subtraction will have to do.

In terms of [Scott Garrabrant's taxonomy](https://www.lesswrong.com/posts/EbFABnst8LsidYs5Y/goodhart-taxonomy) of applications of [Goodhart's law](https://www.lesswrong.com/posts/YtvZxRpZjcFNwJecS/the-importance-of-goodhart-s-law), this is regressional Goodhart: Society _wants_ to select for maturity, chooses age as a proxy, and in the process, ends up granting or withholding privileges that a more discriminating Society maybe wouldn't.

The age of majority is a case of replacing a _complicated_, [illegible](https://www.ribbonfarm.com/2010/07/26/a-big-little-idea-called-legibility/) category ("maturity", the kind of abstract thing you might want to model as a cluster in a forty-dimensional space) with a _simple_ membership test (an age cutoff that everyone knows how to compute).



because different people might make make different judgements of the complicated category

