# function estimate_pi(n)
#     n > 0 || throw(ArgumentError("number of iterations must be >0, got $n"))
#     num_inside = 0
#     for i in 1:n
#         x, y = rand(), rand()
#         if x^2 + y^2 <= 1
#             num_inside += 1
#         end
#     end
#     return 4 * num_inside / n
# end
# estimate_pi(1_000_000)

function est_pi_single(n)
    n > 0 || throw(ArgumentError("number of iterations must be >0, got $n"))
    incircle = 0
    for i in 1:n
        x, y = rand() * 2 - 1, rand() * 2 - 1
        if x^2 + y^2 <= 1
            incircle += 1
        end
    end
    return 4 * incircle / n
end

