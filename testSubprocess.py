#-*- coding:utf-8 -*-

import lupa
from lupa import LuaRuntime
lua = LuaRuntime(unpack_returned_tuples = True)

_= lua.require("cave")

lua_1 = lua.eval("""
    function (caveId)
        local result = {}
        for k,v in pairs(caveData) do
            if k == caveId then
                result = v.progress[1].monster_cfg_ids
                if result then
                    return result
                end
            end
        end
    end
    """
)

d = lua_1(113)
print(d[1])

# lua_2 = lua.eval("""
#     function (test)
#         if test then
#             for k, v in pairs(test) do
#                 print("######  ", k," $$$$$$ ",v )
#             end
#         end
#     end
# """)

# lua_2(d)
