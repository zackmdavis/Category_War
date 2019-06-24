# Schelling Categories, and Simple Membership Tests

**Followup to**: [Where to Draw the Boundaries?](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries)

_Or there might be social or psychological forces anchoring word usages on identifiable Schelling points that are easy for different people to_ agree _upon, even at the cost of some statistical "fit"_ ...

The one comes to you and says, "That paragraph about Schelling points sounded interesting. What did you mean by that? Can you give an example?"

Sure. Previously on _Less Wrong_, in ["The Univariate Fallacy"](https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy), we studied points sampled from two multivariate probability distributions $P_A$ and $P_B$, and showed that it was possible to infer with very high probability which distribution a given point was sampled from, despite significant overlap in the marginal distributions for any one variable considered individually.

From the standpoint of ["the way to carve reality at its joints, is to draw your boundaries around concentrations of unusually high probability density in Thingspace"](https://www.lesswrong.com/posts/yLcuygFfMfrfK8KjF/mutual-information-and-density-in-thingspace), the correct categorization of the points in that example is clear. We have two clearly distinguishable clusters. The [conditional independence](https://www.lesswrong.com/posts/gDWvLicHhcMfGmwaK/conditional-independence-and-naive-bayes) property is satisfied: _given_ a point's cluster-membership, knowing one of the $x_i$ doesn't tell you anything about $x_j$ for _j_ ≠ _i_.

So we should draw a category boundary around each cluster. Obviously. What could _possibly_ change this moral?

_More constraints on the problem_, that's what!

Suppose you needed to _coordinate_ with someone else to make decisions about these points—that is, it's important not just that you and your partner make good decisions, but also [that you make the _same_ decision](https://www.lesswrong.com/posts/9QxnfMYccz9QRgZ5z/the-costly-coordination-mechanism-of-common-knowledge#Coordination_Problems)—but that each of you only got to observe one coordinate from each point. As we saw, the predictive work we get from category-membership in this scenario is spread across _many_ variables: if you only get to observe a _few_ dimensions, you have a lot of uncertainty about cluster-membership (that is, uncertainty about the other dimensions that you haven't observed, but which affect the _ex post_ quality of your decision).

If you and your partner were both ideal Bayesian calculators who could communicate costlessly, you would [share your observations](https://www.overcomingbias.com/2009/02/share-likelihood-ratios-not-posterior-beliefs.html), work out the correct probability, and use that to make optimal decisions. But suppose you _couldn't_ do that—either because communication is expensive, or your partner was bad at math, or any other reason. Then it would be sad if you happened to see $x_9$ = 2 and said "It's an A (probably)!", and your partner happened to see $x_27$ = 3 and said "It's a B (I think)!", and the two of you made inconsistent decisions.

Okay, _now_ suppose that there's actually a forty-first, binary, variable that I didn't tell you about earlier, distributed like so:

$$P_A(x_41) = \begin{cases} 3/4 & x_41 = 0 \\ 1/4 & x_41 = 1 \\ \end{cases}$$

$$P_B(x_41) = \begin{cases} 1/4 & x_41 = 0 \\ 3/4 & x_41 = 1 \\ \end{cases}$$

Observing $x_41$ gives you $\log_2 3$ ≈ 1.585 bits of evidence about cluster-membership, which is more than the

$$\frac{1/4 + 1/16}{2} * |\log_2(4)| + \frac{7/16 + 1/4}{2} * |\log_2(7/4)| + \frac{1/4 + 7/16}{2} * |\log_2(4/7)| + \frac{1/16 + 1/4}{2} * |\log_2(4)|$$

≈ 1.18 bits you can get from any one observation of one of the $x_i$ for _i_ ∈ {1...40}.

If you and your partner can both observe $x_41$, you might end up wanting to base your shared categories and language on _that_—calling a point an "A" if it has $x_41$ = 0, even though such points actually came from $P_B$ a full quarter of the time—even if $x_41$ itself has no effect on the quality of your decisions, and what you _actually_ care about is wholely determined by the values of $x_1$ through $x_40$! It's not the [intension](https://www.lesswrong.com/posts/HsznWM9A7NiuGsp28/extensions-and-intensions) you would pick if you could make (and share) _more observations_—but _ex hypothesi_, you can't.

If you and your partner only get to observe one variable, $x_41$ is your best choice—the single variable that gives you the most information about the "natural" cluster-membership. That also makes it a [_Schelling point_](https://www.lesswrong.com/posts/yJfBzcDL9fBHJfZ6P/nash-equilibria-and-schelling-points)—if you and your partner didn't get to commmunicate in advance about how you want to draw your shared category boundaries, you could pick $x_41$ as your defining observation and be pretty confident your partner would make the same choice. We could imagine an even more pessimistic scenario in which the Schelling point category definition was _less_ predictive than some other candidates—but if you couldn't _coordinate_ to _pick_ one of the more predictive category systems, you might be stuck with the Schelling point.

In conclusion, the right categories to use _given_ constraints on communication and observation, might be different from the categories you would draw from a "God's eye view"—and consideration of which categories are easy for different agents to _coordinate_ is also relevant, in addition to information-theoretic expressive power. Thus, "Schelling categories."

Thanks for reading!

-------

The one says, "No, I meant, like, a _real world_ example, not some dumb math thing for nerds. An _actionable takeaway_ about, like, whether I should support the [Blues or Greens](https://www.lesswrong.com/posts/6hfGNLf4Hg5DXqJCF/a-fable-of-science-and-politics) in the next chariot race—or _at least_ something about dolphins. What is this post _really_ about?"

Oh. One of _those_ readers, I see. Fine, I can probably think of something.

Ummmm ...

Let's see ...

Okay, here's something, maybe. What's the deal the [age of majority](https://en.wikipedia.org/wiki/Age_of_majority)?

Society needs to decide who it wants to be allowed to vote, stand trial, sign contracts, serve in the military, _&c._ Whether it's a good idea for a particular person to have these privileges presumably depends on various _relevant_ features of that person: things like cognitive ability, foresight, wisdom, relevant experiences, _&c_. In particular, it would be _pretty weird_ for someone's fitness to vote to directly depend on _how many times the Earth has gone around the sun since they were born_. What does _that_ number have to do with anything?

It doesn't! But if Society isn't well-coordinated enough to _agree_ on the exact prerequisites for voting and how to measure them, but _can_ agree that most twenty-five-year-olds have them and most eleven-year-olds don't, then we end up choosing some arbitrary age cutoff as the criterion for our "legal adulthood" social construct. It _works_, but it's just a legal fiction—and not necessarily a particularly good fiction, as any bright teenagers reading this will doubtlessly attest.

If I told you that a particular fourteen-year-old was very "mature", that's a contentful statement: we have shared meaning attached to the word _mature_, such that my describing someone that way constrains your anticipations. But it's a _really complicated_ meaning, a statistical signal in behavior that your brain can pick up on, but which isn't particularly verifiable to others who might have reasons to doubt your character assessment. In contrast, age is easy for everyone to agree on. We could imagine some hypothetical science-fictional Society that used brain scans and some sophisticated machine-learning classifer to determine which citizens get which privileges—but in our dumber, poorer world, calendars and subtraction will have to do.

In terms of [Scott Garrabrant's taxonomy](https://www.lesswrong.com/posts/EbFABnst8LsidYs5Y/goodhart-taxonomy) of applications of [Goodhart's law](https://www.lesswrong.com/posts/YtvZxRpZjcFNwJecS/the-importance-of-goodhart-s-law), this is regressional Goodhart: Society _wants_ to select for maturity, chooses age as a proxy, and in the process, ends up granting or withholding privileges that a more discriminating Society maybe wouldn't.

The age of majority is a case of replacing a _complicated_, [illegible](https://www.ribbonfarm.com/2010/07/26/a-big-little-idea-called-legibility/) category ("maturity", the kind of abstract thing you might want to model as a cluster in a forty-dimensional space) with a _simple_ membership test (an age cutoff that everyone knows how to compute).

Simple membership tests don't necessarily have to be objectively measurable properties: it's possible to _delegate_ the category-membership test to more subjective criteria, like the presence of some signal, or the judgement of some canonical authority.

In ["The Ideology Is Not the Movement"](https://slatestarcodex.com/2016/04/04/the-ideology-is-not-the-movement/), the immortal Scott Alexander writes about his model of the genesis of social groups, using atheism as an example—

> Pre-existing differences are the raw materials out of which tribes are made. A good tribe combines people who have similar interests and styles of interaction _even before_ the ethnogenesis event. Any description of these differences will necessarily involve stereotypes, but a lot of them should be hard to argue. [...] There are subtle habits of thought, not yet described by any word or sentence, which atheists are more likely to have than other people. It’s part of the reason why atheists need atheism as a rallying flag instead of just starting the Skeptical Nerdy Male Club.
>
> The rallying flag is the explicit purpose of the tribe. It's usually a belief, event, or activity that get people with that specific pre-existing difference together and excited. Often it brings previously latent differences into sharp relief. People meet around the rallying flag, encounter each other, and say "You seem like a kindred soul!" or "I thought I was the only one!" Usually it suggests some course of action, which provides the tribe with a purpose. For atheists, the rallying flag is not believing in God. Somebody says "Hey, I don't believe in God, if you also don't believe in God come over here and we'll hang out together and talk about how much religious people suck." All the atheists go over by the rallying flag and get very excited about meeting each other. It starts with "Wow, you hate church too?", moves on to "Really, you also like science fiction?", and ends up at "Wow, you have the same undefinable habits of thought that I do!"

We can interpret Alexander's "rallying flag" as a Schelling point for category definition. We don't know how to _talk_ about the preëxisting undefinable habits of thought that make such groups work. (Although we could imagine some hypothetical science-fictional Society that _did_, and consequently had richer forms of social and political organization than our own.) But we _can_ coordinate around whether someone has pledged allegiance to the rallying flag: just _ask_ someone, "Are you an atheist?" and if they say Yes, then they are.

Well, _probably_. We've seen that objective measurements like age are subject to regressional Goodhart, but subjective criteria like self-identification are furthermore subject to _adversarial_ Goodhart: once a category membership test has been established, some agents might have an incentive to create examples that _pass the test_, but don't have the complicated, illegible properties than made the test a useful proxy in the first place.

Consider again the parable about the Sorter of bleggs and rubes who is at first overjoyed to be promoted to "Vice President of Sorting", only to be dismayed to learn that the change in title doesn't come with any material change in responsibilities or working conditions.

Is the new title a _lie_? I think many people would be inclined to say _No_, on the grounds that they expect the "job title" (the words that get printed on business cards or employee rosters or immigration sponsorship forms) to be the canonical description of what someone "does", even if the vagaries of the workday encompass many tasks,[^booth] and an alien anthropologist tasked with observing the worksite and summarizing what each of the humans did might slice up her observations into categories with little resemblance to the company's formal org chart. Since we don't know _how_ to average over all possible alien anthropologists weighted by simplicity, it can't be _lying_ to just go with what the org chart says.

[^booth]: When I worked in a supermarket, two days a week I did Tracy's bookkeeping/customer-service job while Tracy had her weekend, which entailed counting the money from last night's tills _and_ answering the phone _and_ selling money orders _and_ ... I'm actually not sure what official name this role had in Safeway's official org chart. We just called it "the booth."

But "Vice President" has a _literal meaning_. Or it _used to_. _Vice_, ["in place of; subordinate to."](https://en.wiktionary.org/wiki/vice#Etymology_3) _President_, one who _presides_ over some deliberative body.

[This](http://benjaminrosshoffman.com/excerpts-from-a-larger-discussion-about-simulacra/) may constitute a "security vulnerability" in [codes of ethics](https://www.lesswrong.com/posts/xdwbX9pFEr7Pomaxv/meta-honesty-firming-up-honesty-around-its-edge-cases) that have an [ethical injunction](https://www.lesswrong.com/posts/dWTEtgBfFaz6vjwQf/ethical-injunctions) against lying.

_(Thanks to Ben Hoffman for the etymology of "Vice President.")_
