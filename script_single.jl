using JSON3

n = 1_000_000_000

stats = @timed begin
    est_pi_single(n)
end

@info "Finished computation. π estimate: " stats[:value]

results = Dict(
    :pi => stats[:value],
    :num_trials => n,
    :compute_time => stats[:time]
)

open("results_single_jl.json", "w") do io
    JSON3.pretty(io, results)
end

ENV["RESULTS_JL"] = JSON3.pretty(results)
ENV["RESULTS_JL_FILE"] = "results_single_jl.json"