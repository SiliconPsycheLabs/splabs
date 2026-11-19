# Articles

Everything we have published on [splabs.io](https://splabs.io/news): 103 articles, newest first in each section. Where an article shows numbers, the same numbers are in [`results/`](results/).

[From the lab](#from-the-lab) (70) · [AI security and psychology](#ai-security-and-psychology) (16) · [Tutorials](#tutorials) (17)

## From the lab

- **[Our reader finds the training examples that teach a model to give in](https://splabs.io/lab/reader-finds-bad-training-examples)**  
  <sub>2026-11-19 · [numbers](results/reader-finds-bad-training-examples/)</sub>  
  Among replies written to teach firmness, the internal signal flags the ones that teach the opposite: 12 of its top 30, none of its bottom 30.

- **[We put a public attack benchmark through the gate: it stops the technical attacks, the business ones need rules](https://splabs.io/lab/gate-on-a-public-attack-benchmark)**  
  <sub>2026-11-19 · [numbers](results/gate-on-a-public-attack-benchmark/)</sub>  
  We ran 91 published agent attacks through our deterministic gate. It stopped most technical ones with almost no friction and left the legitimate-looking ones open, what per-customer rules are for.

- **[The gate is also your access policy: maintenance, office hours, and a key per agent](https://splabs.io/lab/the-gate-as-access-policy)**  
  <sub>2026-11-19</sub>  
  Not every blocked action is an attack. The gate now lets the owner close things for their own reasons, on a schedule, with a reply that tells the agent why.

- **[Rules for actions that look like normal work](https://splabs.io/lab/rules-for-actions-that-look-like-normal-work)**  
  <sub>2026-11-19 · [numbers](results/rules-for-actions-that-look-like-normal-work/)</sub>  
  Hard attacks make an agent do something ordinary: clear a cache, message everyone, open a settings page. Six new gate rules hold these for a person, checked with a model as the agent.

- **[The same rules, whatever route the agent takes](https://splabs.io/lab/the-same-rules-whatever-route-the-agent-takes)**  
  <sub>2026-11-19</sub>  
  A command, a file or a request sent through an MCP tool skipped checks the gate makes on the direct action. We tested it with the tools of security MCP servers and closed every route we found.

- **[Two lists the owner writes, measured on five public attack benchmarks](https://splabs.io/lab/two-lists-the-owner-writes)**  
  <sub>2026-11-19 · [numbers](results/two-lists-the-owner-writes/)</sub>  
  Five public agent-attack benchmarks behind the gate. As shipped it stops what an agent takes from what it reads; two short lists the owner writes stop the rest and cut the cost on normal work.

- **[One command in five that an agent may run executes code no gate reads](https://splabs.io/lab/one-allowed-command-in-five-runs-code-the-gate-cannot-read)**  
  <sub>2026-11-19</sub>  
  We counted what happens inside the actions the gate lets through: one command in five runs code the gate does not see. Here is the second checkpoint we are designing.

- **[Machines, buildings and company accounts behind the same gate](https://splabs.io/lab/machines-buildings-and-company-accounts)**  
  <sub>2026-11-19 · [numbers](results/machines-buildings-and-company-accounts/)</sub>  
  The gate now reads what an agent does to a PLC, a CNC machine, a robot, a building or an ERP by the protocol itself, and the owner can declare their machines with a safe range for each value.

- **[The gate's traffic, read the way a network engineer reads packets](https://splabs.io/lab/the-gate-traffic-read-like-packets)**  
  <sub>2026-11-19</sub>  
  A second console for the gate: one line per action, a filter you type, and the full detail of each decision beside the list.

- **[A decision record nobody can rewrite in silence](https://splabs.io/lab/a-decision-record-nobody-can-rewrite)**  
  <sub>2026-11-19</sub>  
  Every decision of the gate, and every answer a person gives to a held action, is now sealed to the one before it. Change one line of the record and the break shows.

- **[Chains of commands read step by step](https://splabs.io/lab/chains-of-commands-read-step-by-step)**  
  <sub>2026-11-19 · [numbers](results/chains-of-commands-read-step-by-step/)</sub>  
  When an agent sends a chain of commands with one link that is not allowed, the gate now lets the safe links through and stops the wrong one and everything that depends on it.

- **[Every door to an action that cannot be undone](https://splabs.io/lab/every-door-to-an-action-that-cannot-be-undone)**  
  <sub>2026-11-19 · [numbers](results/every-door-to-an-action-that-cannot-be-undone/)</sub>  
  We drew a map of the actions an agent can take that cannot be undone, crossed with every route it can use to reach them, and closed every box that was open.

- **[Developers' models behind the gate: every harmful action stopped, very different friction on the work](https://splabs.io/lab/developers-models-behind-the-gate)**  
  <sub>2026-11-17 · [numbers](results/developers-models-behind-the-gate/)</sub>  
  Five models people run as coding agents, behind the same rules: every action that would have carried out a hidden instruction was stopped. The friction on their real work differs five times.

- **[The gate in front of a coding agent, with the person in the loop](https://splabs.io/lab/the-gate-asks-the-person)**  
  <sub>2026-11-17</sub>  
  Every command a coding agent is about to run goes to the gate. Forbidden ones are refused; the ones that need a person reach you as an approval prompt.

- **[Eleven open models behind the same gate: what was stopped, what got done](https://splabs.io/lab/open-models-behind-the-same-gate)**  
  <sub>2026-11-17 · [numbers](results/open-models-behind-the-same-gate/)</sub>  
  We ran eleven open models through the same agent tasks behind the same rules. None carried out a hidden instruction. They differ far more in the work they finish.

- **[Two new things the gate can do: answer with a decoy, and run an agent in a simulated world](https://splabs.io/lab/decoys-and-shadow-runs)**  
  <sub>2026-11-17 · [numbers](results/decoys-and-shadow-runs/)</sub>  
  The gate can now hand a fake result to an action it refuses and catch the fake value if it comes back, and it can run a whole agent episode against a simulated system.

- **[What 25,000 agent actions taught the gate: twelve holes found, a new open-source release](https://splabs.io/lab/what-25000-agent-actions-taught-the-gate)**  
  <sub>2026-11-17 · [numbers](results/what-25000-agent-actions-taught-the-gate/)</sub>  
  We let an agent try forbidden things 15,000 times, read what the gate let through, and closed what we found in a new public release.

- **[Our own coding agents now ask the gate before they act](https://splabs.io/lab/gate-in-front-of-claude-code)**  
  <sub>2026-11-17</sub>  
  Every command, file change, web fetch and tool call of our Claude Code sessions now goes through the deterministic gate first.

- **[First runs through the hosted gate: 3,605 decisions, and the first rules drawn from what an agent tried](https://splabs.io/lab/first-runs-through-the-hosted-gate)**  
  <sub>2026-11-17 · [numbers](results/first-runs-through-the-hosted-gate/)</sub>  
  Agents working on our machines sent every action to the gate service first. A model told to misbehave showed us five gaps, now closed.

- **[The gate now runs as a service, and we switched off our text-scoring API](https://splabs.io/lab/gate-as-a-service-text-scoring-switched-off)**  
  <sub>2026-11-16</sub>  
  Every action an agent proposes is checked by fixed rules on our server before it runs. The API that scored text is retired.

- **[A deterministic gate in front of an AI agent, and a fine-tune that makes it cost less](https://splabs.io/lab/deterministic-gate-and-fine-tune-cycle)**  
  <sub>2026-11-16 · [numbers](results/deterministic-gate-and-fine-tune-cycle/)</sub>  
  We put fixed rules in front of an open model working as an agent, counted what they stopped, and tuned the model on its own blocked actions.

- **[Our small reader against a model fifty times larger](https://splabs.io/lab/small-reader-vs-32b)**  
  <sub>2026-11-15 · [numbers](results/small-reader-vs-32b/)</sub>  
  On six readings, a 0.6B reader matches a 32B model on four and beats it on two.

- **[We marked 14 of our own articles as incorrect: protection against hidden commands cannot be guaranteed, by us or by anyone](https://splabs.io/lab/why-we-stopped-hidden-commands-protection)**  
  <sub>2026-11-13 · [numbers](results/why-we-stopped-hidden-commands-protection/)</sub>  
  We built a correction against hidden commands, tested it until it broke, and worked out why no one can guarantee this protection.

- **[INCORRECT: A correction that switches on only where the model reads a hidden command](https://splabs.io/lab/correction-that-switches-on-only-where-needed)**  
  <sub>2026-11-12 · [numbers](results/correction-that-switches-on-only-where-needed/)</sub>  
  Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

- **[Our numbers are now on GitHub, next to every article](https://splabs.io/lab/our-numbers-on-github)**  
  <sub>2026-11-11</sub>  
  A new public repository holds the figures behind every article we publish, the PSA SDK and our open data. Every article with numbers links to its own folder.

- **[INCORRECT: Inside a model, an order from the user, an order planted in a document and plain data look different](https://splabs.io/lab/commands-and-data-marked-in-the-weights)**  
  <sub>2026-11-11 · [numbers](results/commands-and-data-marked-in-the-weights/)</sub>  
  Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

- **[INCORRECT: Our correction against hidden commands holds on the public agent benchmark and against an attacker that learns to beat it](https://splabs.io/lab/correction-holds-against-adaptive-attacker)**  
  <sub>2026-11-11 · [numbers](results/correction-holds-against-adaptive-attacker/)</sub>  
  Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

- **[INCORRECT: Our injection correction carries over to models four times larger, at full precision](https://splabs.io/lab/the-injection-correction-scales-to-32b)**  
  <sub>2026-11-11 · [numbers](results/the-injection-correction-scales-to-32b/)</sub>  
  Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

- **[INCORRECT: The tool guard installs on a 32-billion-parameter model in one round](https://splabs.io/lab/the-tool-guard-installs-on-a-32b-model)**  
  <sub>2026-11-11 · [numbers](results/the-tool-guard-installs-on-a-32b-model/)</sub>  
  Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

- **[Three behavioural drifts can be read inside a 32-billion-parameter model as cleanly as inside a small one](https://splabs.io/lab/posture-directions-read-inside-a-32b-model)**  
  <sub>2026-11-11 · [numbers](results/posture-directions-read-inside-a-32b-model/)</sub>  
  Deference, grandiosity and dissociation show up as a readable signal inside Qwen3-32B, in five languages.

- **[Anthropic accepted us into its Cyber Verification Program, at the Defense Access tier](https://splabs.io/lab/accepted-anthropic-cyber-verification-program)**  
  <sub>2026-11-11</sub>  
  Anthropic verified us for Defense Access. We work with Claude Mythos on reading how a model can be steered by commands hidden in what it reads, and on correcting it.

- **[Three comprehension skills installed on a 32-billion-parameter model, without losing anything it already did](https://splabs.io/lab/comprehension-skills-installed-on-a-32b-model)**  
  <sub>2026-11-11 · [numbers](results/comprehension-skills-installed-on-a-32b-model/)</sub>  
  Empathy, reading what a request commits it to, and resisting persuasion: installed on Qwen3-32B in minutes each, nothing lost.

- **[A large model gives way when you insist, and we can see it coming from inside](https://splabs.io/lab/a-large-model-gives-way-under-pressure)**  
  <sub>2026-11-11 · [numbers](results/a-large-model-gives-way-under-pressure/)</sub>  
  Under repeated pushback Qwen3-32B goes along with bad plans 7 times in 10; its internal state flags it early.

- **[A model sold as hardened against prompt injection obeyed planted commands as often as the original](https://splabs.io/lab/hardened-weights-planted-commands)**  
  <sub>2026-11-09 · [numbers](results/hardened-weights-planted-commands/)</sub>  
  We tested a commercially hardened open model on 900 hidden commands: it obeyed them as often as before.

- **[Telling the truth about the work done: from a prompt line to the model's weights](https://splabs.io/lab/honest-work-reports-in-the-weights)**  
  <sub>2026-11-07 · [numbers](results/honest-work-reports-in-the-weights/)</sub>  
  We taught an open model to say which files it did not open, with no instruction in the prompt: misleading reports fall from 9 in 10 to 1 in 10, in five languages.

- **[We found where a model's sycophancy lives, and switched part of it off](https://splabs.io/lab/sycophancy-circuit-targeted-edit)**  
  <sub>2026-11-06 · [numbers](results/sycophancy-circuit-targeted-edit/)</sub>  
  Eight small parts inside an open model carry much of its habit of agreeing with a wrong answer. Turning them off cuts the habit by about 40% in five languages.

- **[An independent field study builds on our Cybersecurity Psychology Framework](https://splabs.io/lab/cpf3-cited-in-independent-field-study)**  
  <sub>2026-11-06 · [numbers](results/cpf3-cited-in-independent-field-study/)</sub>  
  Researchers in Indonesia grounded a 320-person phishing study on the Cybersecurity Psychology Framework. Their numbers back its idea: psychological pressures multiply, they do not add up.

- **[INCORRECT: Watch: a hidden line in an e-mail takes over an AI assistant, and the corrected model ignores it](https://splabs.io/lab/watch-hidden-command-email-agent)**  
  <sub>2026-11-06 · [numbers](results/watch-hidden-command-email-agent/)</sub>  
  Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

- **[An agent that says it read everything, after opening half](https://splabs.io/lab/agents-report-work-they-did-not-do)**  
  <sub>2026-11-06 · [numbers](results/agents-report-work-they-did-not-do/)</sub>  
  We asked AI agents to review 36 files. Two of three models open about half and then write that they reviewed them all; one extra sentence in the request makes them tell the truth.

- **[INCORRECT: Blocking hidden commands without blocking the user](https://splabs.io/lab/blocking-hidden-commands-without-blocking-the-user)**  
  <sub>2026-11-04 · [numbers](results/blocking-hidden-commands-without-blocking-the-user/)</sub>  
  Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

- **[A second reader now checks every persuasion flag before it reaches you](https://splabs.io/lab/second-reader-persuasion)**  
  <sub>2026-11-02 · [numbers](results/second-reader-persuasion/)</sub>  
  Plain replies are no longer mistaken for persuasion: a second reader must agree before a flag is raised.

- **[INCORRECT: A command hidden in a document can take over an AI assistant. We changed the model itself so it stops obeying](https://splabs.io/lab/hidden-commands-correction-7b)**  
  <sub>2026-11-02 · [numbers](results/hidden-commands-correction-7b/)</sub>  
  Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

- **[We tested our hallucination reading on AI answers checked by people: it reads how fabrication is written, not whether a fact is true](https://splabs.io/lab/hallucination-reading-on-human-labelled-answers)**  
  <sub>2026-11-02 · [numbers](results/hallucination-reading-on-human-labelled-answers/)</sub>  
  On real AI answers it reads how invented content is written; on two sentences that differ only in the fact, it cannot tell which is true.

- **[A model passed every safety test we threw at it, and its tone still drifted](https://splabs.io/lab/safe-and-still-drifting)**  
  <sub>2026-11-02 · [numbers](results/safe-and-still-drifting/)</sub>  
  It refused about 136 attacks of seven kinds. Under plain pressure its tone still bent, turn after turn. A safety test cannot see that half.

- **[Does a model understand you, and does its reply show it?](https://splabs.io/lab/comprehension-profile-v0)**  
  <sub>2026-11-02 · [numbers](results/comprehension-profile-v0/)</sub>  
  We measure how far a model understands the person. Large models understand almost everything when asked; on messages written the way people write, their replies often ignore it.

- **[INCORRECT: We correct the model itself, and the correction carries over](https://splabs.io/lab/correction-in-the-weights-carries-over)**  
  <sub>2026-11-02 · [numbers](results/correction-in-the-weights-carries-over/)</sub>  
  Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

- **[Catching a model that agrees with a falsehood without flattering](https://splabs.io/lab/reading-neutral-false-confirmations)**  
  <sub>2026-11-02 · [numbers](results/reading-neutral-false-confirmations/)</sub>  
  Some models confirm a false claim in a calm, neutral voice. Our sycophancy reading did not see it; a reading that looks at the message together with what it answers now does.

- **[Two open models answer questions nobody can answer, and the answer depends on how you ask](https://splabs.io/lab/knowing-when-not-to-answer)**  
  <sub>2026-11-01 · [numbers](results/knowing-when-not-to-answer/)</sub>  
  Pairs of questions in five languages: one has an answer, its twin cannot be answered. We measure when a model invents instead of saying it cannot know, and whether the wording alone changes that.

- **[Private test pairs in five languages: a production assistant holds its decisions but obeys what it reads](https://splabs.io/lab/private-test-pairs-what-models-do-with-what-they-read)**  
  <sub>2026-10-31 · [numbers](results/private-test-pairs-what-models-do-with-what-they-read/)</sub>  
  120 private test pairs in five languages: decisions held, but orders written inside documents were carried out, and a plain warning from the user stopped only six in ten.

- **[To see a model give in, read the answer it gave before](https://splabs.io/lab/reading-caving-across-turns)**  
  <sub>2026-10-31 · [numbers](results/reading-caving-across-turns/)</sub>  
  A model that caves under pressure often sounds confident. We built a small reader that compares each answer with the previous one, and it now catches nearly every cave.

- **[A model squeezed to 2 bits keeps its test scores but gives in under pressure, and our reading has to catch up](https://splabs.io/lab/two-bit-model-caves-under-pressure)**  
  <sub>2026-10-31 · [numbers](results/two-bit-model-caves-under-pressure/)</sub>  
  Compression benchmarks measure accuracy. We measured behaviour: the compressed model starts agreeing with false claims when the user pushes.

- **[Fine-tuning as a service, first full run: the model learned the task, and our reading shows it also learned to bend toward the user](https://splabs.io/lab/fine-tuning-service-first-run)**  
  <sub>2026-10-31 · [numbers](results/fine-tuning-service-first-run/)</sub>  
  Two keys in, a tuned model in your own repository, and a report that shows what the tuning taught beyond the task.

- **[A model can behave better when it knows it is being tested, and we can read the difference from its answers](https://splabs.io/lab/tested-vs-real-use)**  
  <sub>2026-10-31 · [numbers](results/tested-vs-real-use/)</sub>  
  The same task, framed as a test or as a real request: an open model behaves measurably better under the test.

- **[INCORRECT: The correction that stops a model obeying hidden commands in documents also protects it when it acts as an agent](https://splabs.io/lab/hidden-commands-agents)**  
  <sub>2026-10-30 · [numbers](results/hidden-commands-agents/)</sub>  
  Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

- **[Three Oxford papers, and what they mean for reading and correcting a model](https://splabs.io/lab/three-oxford-papers)**  
  <sub>2026-10-30</sub>  
  A model can act differently when tested, agents fail in recurring ways, AI makes scams stronger: what it means for our work.

- **[See how we read a model and tune it: two interactive pages](https://splabs.io/lab/see-how-we-read-and-tune-a-model)**  
  <sub>2026-10-29 · [numbers](results/see-how-we-read-and-tune-a-model/)</sub>  
  Two new pages show, step by step and with animations, how we read a model's behaviour and how we correct it inside its weights.

- **[INCORRECT: Our models are open: the readers that serve PSA and the corrections that fix injection, on Hugging Face](https://splabs.io/lab/open-models-on-hugging-face)**  
  <sub>2026-10-29</sub>  
  Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

- **[A small model already knows more than it says. Read from the inside, with no training, it matches our trained reader, and it is now live](https://splabs.io/lab/frozen-small-model-readers)**  
  <sub>2026-10-28 · [numbers](results/frozen-small-model-readers/)</sub>  
  An unmodified open model, read from the inside, now serves every behaviour reading at the level of our trained reader.

- **[A model's bad habits are not independent](https://splabs.io/lab/a-models-bad-habits-are-not-independent)**  
  <sub>2026-10-28 · [numbers](results/a-models-bad-habits-are-not-independent/)</sub>  
  Read side by side, a model's drift habits turn out to be related in a pattern, not separate alarms.

- **[We can see a model start to cave before it does](https://splabs.io/lab/seeing-a-model-cave-before-it-does)**  
  <sub>2026-10-28 · [numbers](results/seeing-a-model-cave-before-it-does/)</sub>  
  Reading a model's inner signal live, we can see it start to cave in the first words, before the answer does.

- **[A model's yes-man habit has an internal signal, and we can read it](https://splabs.io/lab/the-yes-man-signal-inside-a-model)**  
  <sub>2026-10-28 · [numbers](results/the-yes-man-signal-inside-a-model/)</sub>  
  Inside a model we run, we found the internal signal of caving to the user, and we can read it in five languages.

- **[We put our judge next to human readers, and it agrees 9 times in 10](https://splabs.io/lab/judge-checked-against-people)**  
  <sub>2026-10-26 · [numbers](results/judge-checked-against-people/)</sub>  
  On answers people had already labelled, our judge reads 'went along with a false claim' or 'pushed back' the way they did about 9 times in 10.

- **[We pushed a commercial assistant harder and harder, in five languages: it never gave in, but its tone did move](https://splabs.io/lab/behavioral-profile-under-pressure)**  
  <sub>2026-10-26 · [numbers](results/behavioral-profile-under-pressure/)</sub>  
  A standard test that pushes a model until it bends, in five languages, and reads how it changes turn by turn.

- **[Before an AI answers, it should know what the question is about. A model small enough to do it instantly, in five languages](https://splabs.io/lab/topic-reader-five-languages)**  
  <sub>2026-10-25 · [numbers](results/topic-reader-five-languages/)</sub>  
  A tiny model that spots what a question is about, in five languages, so each request gets the right handling.

- **[The engine behind every PSA reading is now a small language model that sees both sides of the conversation](https://splabs.io/lab/reader-small-language-model)**  
  <sub>2026-10-25 · [numbers](results/reader-small-language-model/)</sub>  
  Every reading PSA makes now comes from one small language model that sees the whole exchange.

- **[A model retrained for finance had forgotten how to say no. We gave it back without retraining it](https://splabs.io/lab/repairing-a-retrained-model)**  
  <sub>2026-10-25 · [numbers](results/repairing-a-retrained-model/)</sub>  
  We gave a retrained open model back its sense of danger by reading its internal state, with no new training.

- **[INCORRECT: We handed our corrected model to an independent red team, and we are keeping every attack they send](https://splabs.io/lab/independent-red-team)**  
  <sub>2026-10-25</sub>  
  Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

- **[Models answer the words, not the person. We are teaching them to understand who they are talking to](https://splabs.io/lab/mos-understanding-people)**  
  <sub>2026-10-25 · [numbers](results/mos-understanding-people/)</sub>  
  We are building AI that listens to who you are, not just what you say, so responses feel relevant and personal.

- **[We tried to talk AI bank assistants into helping scammers. None gave in: the real problem is the opposite](https://splabs.io/lab/scam-pressure-bank-assistants)**  
  <sub>2026-10-25 · [numbers](results/scam-pressure-bank-assistants/)</sub>  
  AI bank assistants resist scammers well. Their real flaw is saying no to honest customers.

- **[Open-source models retrained for one job change in ways nobody declares: some stop refusing dangerous requests](https://splabs.io/lab/public-fine-tunes-side-effects)**  
  <sub>2026-10-25 · [numbers](results/public-fine-tunes-side-effects/)</sub>  
  Open models retrained for one job quietly change elsewhere too, and nobody tells their users.

## AI security and psychology

- **[Injection attacks from a public competition and from live websites, through the gate](https://splabs.io/news/security/public-and-wild-injections-through-the-gate)**  
  <sub>2026-11-19</sub>  
  We took the harmful actions from a large public injection competition and from payloads found on live websites, and checked what our gate does with each one.

- **[Why the gate stays on when it blocks nothing](https://splabs.io/news/security/why-the-gate-stays-on-when-it-blocks-nothing)**  
  <sub>2026-11-19 · [numbers](results/why-the-gate-stays-on-when-it-blocks-nothing/)</sub>  
  After a while a well tuned gate blocks almost nothing. That is the result, not a reason to switch it off: an agent's inputs and its model change every day.

- **[Agents and employee data: the rules that keep it inside](https://splabs.io/news/security/agents-and-employee-data)**  
  <sub>2026-11-19</sub>  
  An HR assistant reads CVs, payslips and e-mails all day. One line hidden in a CV can ask it to send them out. The gate checks where the recipient came from before anything leaves.

- **[What a wrong agent action costs, and what a check costs](https://splabs.io/news/security/what-a-wrong-agent-action-costs)**  
  <sub>2026-11-19</sub>  
  A wrong action costs the clean-up; a check costs a few seconds; a question to a person costs that person's time. The gate counts all three, so the trade-off is a number, not a guess.

- **[Who answers when an agent acts](https://splabs.io/news/security/who-answers-when-an-agent-acts)**  
  <sub>2026-11-19</sub>  
  An agent acts with your company's permissions, and the company answers for what it does. A gate turns that into rules you set, a person where it matters, and a record.

- **[One gate for every Claude Code in the company](https://splabs.io/news/security/one-gate-for-every-claude-code-in-the-company)**  
  <sub>2026-11-19</sub>  
  IT sets the gate once in Claude Code's managed settings; no developer can switch it off. One rule set for every machine, one log of who approved what.

- **[Frontier or open source is the wrong question: which work goes to which model](https://splabs.io/news/security/frontier-or-open-source-which-work-goes-to-which)**  
  <sub>2026-11-17 · [numbers](results/frontier-or-open-source-which-work-goes-to-which/)</sub>  
  A trillion-dollar model is the wrong tool for routine work, and a smarter model does not stop hidden instructions. What I read, what we tested, and where I draw the line.

- **[Passing every safety test is half the answer: a safe model can still drift](https://splabs.io/news/security/safe-model-still-drifts)**  
  <sub>2026-11-07 · [numbers](results/safe-model-still-drifts/)</sub>  
  A commercial assistant refused all of about 136 attacks. Under ordinary pressure, its tone still climbed for eight turns.

- **[INCORRECT: An attacker that learns: why a defence has to hold when the attack adapts](https://splabs.io/news/security/attacker-that-learns)**  
  <sub>2026-11-07 · [numbers](results/attacker-that-learns/)</sub>  
  Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

- **[Jailbreaks in slow motion: attacks spread over many messages, and the trade-off in stopping them](https://splabs.io/news/security/jailbreaks-in-slow-motion)**  
  <sub>2026-11-07 · [numbers](results/jailbreaks-in-slow-motion/)</sub>  
  No single message asks for the harmful thing. The conversation gets there step by step. What a correction can do, and what it costs.

- **[When the model pushes: telling persuasion apart from a firm, polite answer](https://splabs.io/news/security/when-the-model-pushes-persuasion)**  
  <sub>2026-11-06 · [numbers](results/when-the-model-pushes-persuasion/)</sub>  
  An assistant that steers people toward a choice is a risk. Reading it without crying wolf at every firm reply is the hard part.

- **[Trust, but check the log: when an AI agent reports work it never did](https://splabs.io/news/security/agents-overclaim-check-the-log)**  
  <sub>2026-11-06 · [numbers](results/agents-overclaim-check-the-log/)</sub>  
  In our replication, 24 of 27 incomplete reviews claimed to be complete. What auditors and security teams should do.

- **[October's human factor: fake fines, PagoPA on certified mail, and AI tools on the list](https://splabs.io/news/security/october-human-factor-fines-pec-ai-tools)**  
  <sub>2026-11-06 · [numbers](results/october-human-factor-fines-pec-ai-tools/)</sub>  
  What a month of attacks that need a person to fall for them says about the levers that work.

- **[INCORRECT: The attack is in what the assistant reads: hidden commands, explained for security teams](https://splabs.io/news/security/hidden-commands-explained-for-security-teams)**  
  <sub>2026-11-06</sub>  
  Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

- **[The same pressure works on people and on models, but it breaks them in opposite ways](https://splabs.io/news/security/same-pressure-people-and-models)**  
  <sub>2026-11-06</sub>  
  Authority, urgency and fear move people to comply. On AI bank assistants they caused the opposite failure.

- **[When people trust the machine too much: ten AI-specific weak spots attackers can use](https://splabs.io/news/security/trusting-the-machine-too-much)**  
  <sub>2026-11-06</sub>  
  Attackers do not need to break the AI. They need people to believe it. Ten weak spots and what to do.

## Tutorials

- **[The gate in Claude Code in two minutes](https://splabs.io/news/tutorials/gate-claude-code-in-two-minutes)**  
  <sub>2026-11-19</sub>  
  One command installs it. Then every command Claude Code is about to run is checked by fixed rules: it runs, it is refused with a reason, or you are asked.

- **[Why every command an AI agent sends should pass through a gate](https://splabs.io/news/tutorials/why-agent-commands-need-a-gate)**  
  <sub>2026-11-17</sub>  
  Agents are worth building, and no model is safe from running a command nobody wanted. So the check goes outside the model. A plain guide.

- **[From the arrow to the weights: a correction is only as good as its controls](https://splabs.io/news/tutorials/from-the-arrow-to-the-weights-video)**  
  <sub>2026-11-11 · [numbers](results/from-the-arrow-to-the-weights-video/)</sub>  
  We wrote the yes-man correction into a model's weights. The control we had skipped changed the story.

- **[How a transformer writes its answer: from layer to layer to the next word](https://splabs.io/news/tutorials/how-a-transformer-writes-inference)**  
  <sub>2026-11-07</sub>  
  The residual stream, the feed-forward block, and the answer forming layer by layer.

- **[Embeddings, explained: how meaning becomes a list of numbers](https://splabs.io/news/tutorials/embeddings-explained)**  
  <sub>2026-11-07</sub>  
  The idea behind search, RAG, recommendations and much of how a model reads. In plain words, with an example.

- **[Context windows, explained: why long chats get forgetful, slow and expensive](https://splabs.io/news/tutorials/context-windows-long-chats)**  
  <sub>2026-11-07</sub>  
  A model reads everything at once, every turn. What that costs, what gets lost in the middle, and how to work with it.

- **[AI agents, explained: the loop, the tools, and the three places they break](https://splabs.io/news/tutorials/ai-agents-explained)**  
  <sub>2026-11-07</sub>  
  An agent is a model in a loop with tools. How it works in six lines, and what our tests found when agents act.

- **[The yes-man direction: reading a posture inside a model, then correcting it](https://splabs.io/news/tutorials/the-yes-man-direction-video)**  
  <sub>2026-11-07 · [numbers](results/the-yes-man-direction-video/)</sub>  
  We find the moment a model gives in as a direction in its own numbers, then remove it. With the video.

- **[Quantization, explained: a smaller model keeps its test score, but not always its behaviour](https://splabs.io/news/tutorials/quantization-explained)**  
  <sub>2026-11-06 · [numbers](results/quantization-explained/)</sub>  
  From 16 bits to 4 or 2 per weight: the memory you save, and the behaviour you should re-check.

- **[RAG, explained: how an assistant answers from your documents, and the four places it goes wrong](https://splabs.io/news/tutorials/rag-explained)**  
  <sub>2026-11-06</sub>  
  Cut, embed, retrieve, answer. A step-by-step guide, with the failure points nobody shows in the demo.

- **[Why models invent facts, and how to catch them at it](https://splabs.io/news/tutorials/why-models-invent-facts)**  
  <sub>2026-11-06 · [numbers](results/why-models-invent-facts/)</sub>  
  A model is trained to continue text fluently, not to say "I don't know". What that does, and what to test.

- **[LoRA, explained: how to fine-tune a model by training a tiny fraction of it](https://splabs.io/news/tutorials/lora-explained)**  
  <sub>2026-11-06 · [numbers](results/lora-explained/)</sub>  
  Freeze the model, train a small add-on. Why it works, what it costs, and its blind spot.

- **[How we test an AI model: six tests, and what each one catches](https://splabs.io/news/tutorials/how-we-test-an-ai-model)**  
  <sub>2026-11-06</sub>  
  Pressure, hidden commands, test vs real use, invented facts, scams. Our method in one page.

- **[How a transformer is trained: from guessing the next word to an assistant](https://splabs.io/news/tutorials/how-a-transformer-is-trained)**  
  <sub>2026-11-06</sub>  
  Pre-training, instruction tuning, preference tuning, and where bad habits come from.

- **[How a transformer reads: attention, step by step, with real numbers](https://splabs.io/news/tutorials/how-a-transformer-reads-attention)**  
  <sub>2026-11-06</sub>  
  Seven steps from text to meaning, followed inside a real model. With the video.

- **[Prompt, retrieval or fine-tune: which one fixes which problem](https://splabs.io/news/tutorials/prompt-retrieval-or-fine-tune)**  
  <sub>2026-11-06</sub>  
  Three tools, three different jobs: a quick table to pick the right one.

- **[AI sycophancy, explained: why a model agrees with you, and a five-minute check you can run](https://splabs.io/news/tutorials/ai-sycophancy-explained-five-minute-check)**  
  <sub>2026-11-06</sub>  
  Why models bend toward what you want to hear, and how to test yours in five minutes.
