;; EXACT selected function excerpts from module.wat.gz.
;; This is an excerpt, NOT a complete executable module. Function names below are export names, not inferred internals.
;; Each capture is capped near50KB; large functions may end mid-body. Full function byte spans,signatures and complete call-site inventories remain available.
;; Each capture is capped near50KB; large functions may end mid-body. Full function byte spans,signatures and complete call-site inventories remain available.
;; Each capture is capped near50KB; large functions may end mid-body. Full function byte spans,signatures and complete call-site inventories remain available.
;; Exports: uci_command
  (func (;168;) (type 0) (param i32)
    (local i32 i32 i32 i32 i32 i32)
    global.get 2
    i32.const 2
    i32.eq
    if  ;; label = @1
      global.get 3
      global.get 3
      i32.load
      i32.const 20
      i32.sub
      i32.store
      global.get 3
      i32.load
      local.tee 3
      i32.load
      local.set 0
      local.get 3
      i32.load offset=4
      local.set 2
      local.get 3
      i32.load offset=12
      local.set 4
      local.get 3
      i32.load offset=16
      local.set 6
      local.get 3
      i32.load offset=8
      local.set 1
    end
    block (result i32)  ;; label = @1
      global.get 2
      i32.const 2
      i32.eq
      if  ;; label = @2
        global.get 3
        global.get 3
        i32.load
        i32.const 4
        i32.sub
        i32.store
        global.get 3
        i32.load
        i32.load
        local.set 5
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        global.get 0
        i32.const 16
        i32.sub
        local.tee 2
        global.set 0
        local.get 0
        call 22186
        local.tee 4
        i32.const 2147483639
        i32.lt_u
        local.set 1
      end
      local.get 1
      global.get 2
      i32.const 2
      i32.eq
      i32.or
      if  ;; label = @2
        local.get 1
        local.get 4
        i32.const 10
        i32.le_u
        global.get 2
        select
        local.set 1
        block  ;; label = @3
          global.get 2
          i32.eqz
          if  ;; label = @4
            local.get 1
            if  ;; label = @5
              local.get 2
              local.get 4
              i32.store8 offset=15
              local.get 2
              i32.const 4
              i32.add
              local.set 1
              br 2 (;@3;)
            end
            local.get 4
            i32.const 2147483640
            i32.and
            local.tee 6
            i32.const 8
            i32.add
            local.set 1
          end
          global.get 2
          i32.eqz
          local.get 5
          i32.eqz
          i32.or
          if  ;; label = @4
            local.get 1
            call 22866
            local.set 3
            i32.const 0
            global.get 2
            i32.const 1
            i32.eq
            br_if 3 (;@1;)
            drop
            local.get 3
            local.set 1
          end
          global.get 2
          i32.eqz
          if  ;; label = @4
            local.get 2
            local.get 6
            i32.const 2147483640
            i32.sub
            i32.store offset=12
            local.get 2
            local.get 4
            i32.store offset=8
            local.get 2
            local.get 1
            i32.store offset=4
          end
        end
        global.get 2
        i32.eqz
        if  ;; label = @3
          local.get 4
          if  ;; label = @4
            local.get 1
            local.get 0
            local.get 4
            memory.copy
          end
          local.get 1
          local.get 4
          i32.add
          i32.const 0
          i32.store8
          i32.const 18297676
          i32.const 0
          i32.store
          local.get 2
          i32.const 4
          i32.add
          local.set 0
        end
        global.get 2
        i32.eqz
        local.get 5
        i32.const 1
        i32.eq
        i32.or
        if  ;; label = @3
          i32.const 19
          local.get 0
          call 8
          i32.const 1
          global.get 2
          i32.const 1
          i32.eq
          br_if 2 (;@1;)
          drop
        end
        global.get 2
        i32.eqz
        if  ;; label = @3
          i32.const 18297676
          i32.load
          local.set 4
          i32.const 18297676
          i32.const 0
          i32.store
          local.get 4
          i32.const 1
          i32.ne
          if  ;; label = @4
            local.get 2
            i32.load8_s offset=15
            i32.const 0
            i32.lt_s
            if  ;; label = @5
              local.get 2
              i32.load offset=12
              drop
              local.get 2
              i32.load offset=4
              call 22239
            end
            local.get 2
            i32.const 16
            i32.add
            global.set 0
            return
          end
          call 9
          local.set 4
          local.get 2
          i32.load8_s offset=15
          i32.const 0
          i32.lt_s
          if  ;; label = @4
            local.get 2
            i32.load offset=12
            drop
            local.get 2
            i32.load offset=4
            call 22239
          end
          local.get 4
          call 12
          unreachable
        end
      end
      global.get 2
      i32.eqz
      local.get 5
      i32.const 2
      i32.eq
      i32.or
      if  ;; label = @2
        call 169
        i32.const 2
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        unreachable
      end
      return
    end
    local.set 3
    global.get 3
    i32.load
    local.get 3
    i32.store
    global.get 3
    global.get 3
    i32.load
    i32.const 4
    i32.add
    i32.store
    global.get 3
    i32.load
    local.tee 3
    local.get 0
    i32.store
    local.get 3
    local.get 2
    i32.store offset=4
    local.get 3
    local.get 1
    i32.store offset=8
    local.get 3
    local.get 4
    i32.store offset=12
    local.get 3
    local.get 6
    i32.store offset=16
    global.get 3
    global.get 3
    i32.load
    i32.const 20
    i32.add
    i32.store)
;; Exports: init
  (func (;170;) (type 12)
    (local i32 i32 i32 i32 i32 i32)
    global.get 2
    i32.const 2
    i32.eq
    if  ;; label = @1
      global.get 3
      global.get 3
      i32.load
      i32.const 16
      i32.sub
      i32.store
      global.get 3
      i32.load
      local.tee 2
      i32.load
      local.set 0
      local.get 2
      i32.load offset=8
      local.set 3
      local.get 2
      i32.load offset=12
      local.set 4
      local.get 2
      i32.load offset=4
      local.set 1
    end
    block (result i32)  ;; label = @1
      global.get 2
      i32.const 2
      i32.eq
      if  ;; label = @2
        global.get 3
        global.get 3
        i32.load
        i32.const 4
        i32.sub
        i32.store
        global.get 3
        i32.load
        i32.load
        local.set 5
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        global.get 0
        i32.const 16
        i32.sub
        local.tee 3
        global.set 0
        global.get 0
        i32.const 16
        i32.sub
        local.tee 1
        global.set 0
        local.get 1
        i32.const 4
        i32.add
        local.set 0
      end
      global.get 2
      i32.eqz
      local.get 5
      i32.eqz
      i32.or
      if  ;; label = @2
        local.get 0
        call 13140
        i32.const 0
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 18297676
        i32.const 0
        i32.store
        local.get 1
        i32.const 4
        i32.add
        local.set 0
      end
      global.get 2
      i32.eqz
      local.get 5
      i32.const 1
      i32.eq
      i32.or
      if  ;; label = @2
        i32.const 16701
        local.get 3
        local.get 0
        i32.const 235084
        call 4
        i32.const 1
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 18297676
        i32.load
        local.set 4
        i32.const 18297676
        i32.const 0
        i32.store
        block  ;; label = @3
          local.get 4
          i32.const 1
          i32.ne
          if  ;; label = @4
            local.get 1
            i32.load8_s offset=15
            i32.const 0
            i32.lt_s
            if  ;; label = @5
              local.get 1
              i32.load offset=12
              drop
              local.get 1
              i32.load offset=4
              call 22239
            end
            local.get 1
            i32.const 16
            i32.add
            global.set 0
            br 1 (;@3;)
          end
          call 9
          local.set 4
          local.get 1
          i32.load8_s offset=15
          i32.const 0
          i32.lt_s
          if  ;; label = @4
            local.get 1
            i32.load offset=12
            drop
            local.get 1
            i32.load offset=4
            call 22239
          end
          local.get 4
          call 12
          unreachable
        end
        i32.const 18297676
        i32.const 0
        i32.store
        local.get 3
        i32.load
        local.get 3
        local.get 3
        i32.load8_s offset=11
        local.tee 1
        i32.const 0
        i32.lt_s
        local.tee 0
        select
        local.set 4
        local.get 3
        i32.load offset=4
        local.get 1
        local.get 0
        select
        local.set 1
      end
      global.get 2
      i32.eqz
      local.get 5
      i32.const 2
      i32.eq
      i32.or
      if  ;; label = @2
        i32.const 3
        i32.const 18299004
        local.get 4
        local.get 1
        call 5
        local.set 2
        i32.const 2
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
        local.get 2
        local.set 1
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 18297676
        i32.load
        local.set 0
        i32.const 18297676
        i32.const 0
        i32.store
        local.get 0
        i32.const 1
        i32.eq
        local.set 0
      end
      block  ;; label = @2
        block  ;; label = @3
          block  ;; label = @4
            global.get 2
            i32.eqz
            if  ;; label = @5
              local.get 0
              br_if 1 (;@4;)
              local.get 1
              i32.load
              i32.const 12
              i32.sub
              i32.load
              local.set 0
              i32.const 18297676
              i32.const 0
              i32.store
              local.get 3
              i32.const 12
              i32.add
              local.tee 4
              local.get 0
              local.get 1
              i32.add
              call 22501
              i32.const 18297676
              i32.load
              local.set 0
              i32.const 18297676
              i32.const 0
              i32.store
              local.get 0
              i32.const 1
              i32.eq
              br_if 1 (;@4;)
              i32.const 18297676
              i32.const 0
              i32.store
              local.get 3
              i32.const 12
              i32.add
              local.set 0
            end
            global.get 2
            i32.eqz
            local.get 5
            i32.const 3
            i32.eq
            i32.or
            if  ;; label = @5
              i32.const 10
              local.get 0
              i32.const 18300392
              call 13
              local.set 2
              i32.const 3
              global.get 2
              i32.const 1
              i32.eq
              br_if 4 (;@1;)
              drop
              local.get 2
              local.set 0
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              i32.const 18297676
              i32.load
              local.set 4
              i32.const 18297676
              i32.const 0
              i32.store
              local.get 4
              i32.const 1
              i32.ne
              local.set 4
            end
            block  ;; label = @5
              local.get 4
              global.get 2
              i32.const 2
              i32.eq
              i32.or
              if  ;; label = @6
                global.get 2
                i32.eqz
                if  ;; label = @7
                  local.get 0
                  i32.load
                  i32.load offset=28
                  local.set 4
                  i32.const 18297676
                  i32.const 0
                  i32.store
                end
                global.get 2
                i32.eqz
                local.get 5
                i32.const 4
                i32.eq
                i32.or
                if  ;; label = @7
                  local.get 4
                  local.get 0
                  i32.const 10
                  call 13
                  local.set 2
                  i32.const 4
                  global.get 2
                  i32.const 1
                  i32.eq
                  br_if 6 (;@1;)
                  drop
                  local.get 2
                  local.set 4
                end
                global.get 2
                i32.eqz
                if  ;; label = @7
                  i32.const 18297676
                  i32.load
                  local.set 0
                  i32.const 18297676
                  i32.const 0
                  i32.store
                  local.get 0
                  i32.const 1
                  i32.ne
                  local.tee 0
                  br_if 2 (;@5;)
                end
              end
              global.get 2
              i32.eqz
              if  ;; label = @6
                call 9
                local.set 1
                local.get 3
                i32.const 12
                i32.add
                local.set 0
              end
              global.get 2
              i32.eqz
              local.get 5
              i32.const 5
              i32.eq
              i32.or
              if  ;; label = @6
                local.get 0
                call 22753
                local.set 2
                i32.const 5
                global.get 2
                i32.const 1
                i32.eq
                br_if 5 (;@1;)
                drop
                local.get 2
                local.set 0
              end
              global.get 2
              i32.eqz
              br_if 2 (;@3;)
            end
            local.get 0
            local.get 3
            i32.const 12
            i32.add
            global.get 2
            select
            local.set 0
            global.get 2
            i32.eqz
            local.get 5
            i32.const 6
            i32.eq
            i32.or
            if  ;; label = @5
              local.get 0
              call 22753
              drop
              i32.const 6
              global.get 2
              i32.const 1
              i32.eq
              br_if 4 (;@1;)
              drop
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              i32.const 18297676
              i32.const 0
              i32.store
            end
            global.get 2
            i32.eqz
            local.get 5
            i32.const 7
            i32.eq
            i32.or
            if  ;; label = @5
              i32.const 17
              local.get 1
              local.get 4
              call 13
              drop
              i32.const 7
              global.get 2
              i32.const 1
              i32.eq
              br_if 4 (;@1;)
              drop
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              i32.const 18297676
              i32.load
              local.set 0
              i32.const 18297676
              i32.const 0
              i32.store
              local.get 0
              i32.const 1
              i32.eq
              br_if 1 (;@4;)
              i32.const 18297676
              i32.const 0
              i32.store
            end
            global.get 2
            i32.eqz
            local.get 5
            i32.const 8
            i32.eq
            i32.or
            if  ;; label = @5
              i32.const 18
              local.get 1
              call 6
              local.set 2
              i32.const 8
              global.get 2
              i32.const 1
              i32.eq
              br_if 4 (;@1;)
              drop
              local.get 2
              local.set 1
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              i32.const 18297676
              i32.load
              local.set 1
              i32.const 18297676
              i32.const 0
              i32.store
              local.get 1
              i32.const 1
              i32.eq
              local.tee 1
              br_if 1 (;@4;)
              local.get 3
              i32.load8_s offset=11
              i32.const 0
              i32.lt_s
              local.tee 1
              if  ;; label = @6
                local.get 3
                i32.load offset=8
                drop
                local.get 3
                i32.load
                local.tee 1
                call 22239
              end
            end
            global.get 2
            i32.eqz
            local.get 5
            i32.const 9
            i32.eq
            i32.or
            if  ;; label = @5
              i32.const 1
              call 252
              i32.const 9
              global.get 2
              i32.const 1
              i32.eq
              br_if 4 (;@1;)
              drop
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              local.get 3
              i32.const 16
              i32.add
              global.set 0
              br 3 (;@2;)
            end
          end
          global.get 2
          i32.eqz
          if  ;; label = @4
            call 9
            local.set 1
          end
        end
        global.get 2
        i32.eqz
        if  ;; label = @3
          local.get 3
          i32.load8_s offset=11
          i32.const 0
          i32.lt_s
          if  ;; label = @4
            local.get 3
            i32.load offset=8
            drop
            local.get 3
            i32.load
            call 22239
          end
          local.get 1
          call 12
          unreachable
        end
      end
      return
    end
    local.set 2
    global.get 3
    i32.load
    local.get 2
    i32.store
    global.get 3
    global.get 3
    i32.load
    i32.const 4
    i32.add
    i32.store
    global.get 3
    i32.load
    local.tee 2
    local.get 0
    i32.store
    local.get 2
    local.get 1
    i32.store offset=4
    local.get 2
    local.get 3
    i32.store offset=8
    local.get 2
    local.get 4
    i32.store offset=12
    global.get 3
    global.get 3
    i32.load
    i32.const 16
    i32.add
    i32.store)
;; Exports: CEE_InitWithOpts
  (func (;1666;) (type 1) (param i32 i32)
    (local i32)
    global.get 2
    i32.const 2
    i32.eq
    if  ;; label = @1
      global.get 3
      global.get 3
      i32.load
      i32.const 8
      i32.sub
      i32.store
      global.get 3
      i32.load
      local.tee 1
      i32.load
      local.set 0
      local.get 1
      i32.load offset=4
      local.set 1
    end
    block (result i32)  ;; label = @1
      global.get 2
      i32.eqz
      global.get 2
      i32.const 2
      i32.eq
      if (result i32)  ;; label = @2
        global.get 3
        global.get 3
        i32.load
        i32.const 4
        i32.sub
        i32.store
        global.get 3
        i32.load
        i32.load
      else
        local.get 2
      end
      i32.eqz
      i32.or
      if  ;; label = @2
        local.get 0
        local.get 1
        call 1664
        i32.const 0
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
      end
      return
    end
    local.set 2
    global.get 3
    i32.load
    local.get 2
    i32.store
    global.get 3
    global.get 3
    i32.load
    i32.const 4
    i32.add
    i32.store
    global.get 3
    i32.load
    local.tee 2
    local.get 0
    i32.store
    local.get 2
    local.get 1
    i32.store offset=4
    global.get 3
    global.get 3
    i32.load
    i32.const 8
    i32.add
    i32.store)
;; Exports: CEE_Init
  (func (;1667;) (type 12)
    (local i32 i32 i32)
    global.get 2
    i32.const 2
    i32.eq
    if  ;; label = @1
      global.get 3
      global.get 3
      i32.load
      i32.const 4
      i32.sub
      i32.store
      global.get 3
      i32.load
      i32.load
      local.set 0
    end
    block (result i32)  ;; label = @1
      global.get 2
      i32.const 2
      i32.eq
      if  ;; label = @2
        global.get 3
        global.get 3
        i32.load
        i32.const 4
        i32.sub
        i32.store
        global.get 3
        i32.load
        i32.load
        local.set 2
      end
      global.get 2
      i32.eqz
      local.get 2
      i32.eqz
      i32.or
      if  ;; label = @2
        call 22950
        local.set 1
        i32.const 0
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
        local.get 1
        local.set 0
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 2
        local.get 0
        local.get 0
        i32.const 2
        i32.le_s
        select
        local.tee 0
        i32.const 9
        i32.ge_s
        local.set 1
        i32.const 9
        local.get 0
        local.get 1
        select
        i32.const 1
        i32.sub
        local.set 0
      end
      global.get 2
      i32.eqz
      local.get 2
      i32.const 1
      i32.eq
      i32.or
      if  ;; label = @2
        i32.const 1
        local.get 0
        call 1664
        i32.const 1
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
      end
      return
    end
    local.set 1
    global.get 3
    i32.load
    local.get 1
    i32.store
    global.get 3
    global.get 3
    i32.load
    i32.const 4
    i32.add
    i32.store
    global.get 3
    i32.load
    local.get 0
    i32.store
    global.get 3
    global.get 3
    i32.load
    i32.const 4
    i32.add
    i32.store)
;; Exports: CEE_NewFeature
  (func (;1694;) (type 10) (param i32 i32 i32 i32) (result i32)
    (local i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32)
    global.get 2
    i32.const 2
    i32.eq
    if  ;; label = @1
      global.get 3
      global.get 3
      i32.load
      i32.const 56
      i32.sub
      i32.store
      global.get 3
      i32.load
      local.tee 4
      i32.load
      local.set 0
      local.get 4
      i32.load offset=8
      local.set 2
      local.get 4
      i32.load offset=12
      local.set 3
      local.get 4
      i32.load offset=16
      local.set 5
      local.get 4
      i32.load offset=20
      local.set 6
      local.get 4
      i32.load offset=24
      local.set 8
      local.get 4
      i32.load offset=28
      local.set 10
      local.get 4
      i32.load offset=32
      local.set 9
      local.get 4
      i32.load offset=36
      local.set 11
      local.get 4
      i32.load offset=40
      local.set 12
      local.get 4
      i32.load offset=44
      local.set 13
      local.get 4
      i32.load offset=48
      local.set 14
      local.get 4
      i32.load offset=52
      local.set 15
      local.get 4
      i32.load offset=4
      local.set 1
    end
    block (result i32)  ;; label = @1
      global.get 2
      i32.const 2
      i32.eq
      if  ;; label = @2
        global.get 3
        global.get 3
        i32.load
        i32.const 4
        i32.sub
        i32.store
        global.get 3
        i32.load
        i32.load
        local.set 7
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        global.get 0
        local.tee 8
        i32.const 32
        i32.sub
        local.tee 11
        global.set 0
      end
      global.get 2
      i32.eqz
      local.get 7
      i32.eqz
      i32.or
      if  ;; label = @2
        call 1943
        i32.const 0
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 12158592
        call 1695
        local.get 11
        i32.const 8
        i32.add
        local.set 15
        local.get 0
        local.set 10
        global.get 0
        local.tee 14
        i32.const 32
        i32.sub
        local.tee 6
        global.set 0
        local.get 3
        local.set 8
        local.get 1
        local.set 12
      end
      global.get 2
      i32.eqz
      local.get 7
      i32.const 1
      i32.eq
      i32.or
      if  ;; label = @2
        i32.const 24
        call 22866
        local.set 4
        i32.const 1
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
        local.get 4
        local.set 5
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 18297676
        i32.const 0
        i32.store
      end
      global.get 2
      i32.eqz
      local.get 7
      i32.const 2
      i32.eq
      i32.or
      if  ;; label = @2
        i32.const 2279
        local.get 5
        i32.const 0
        i32.const 0
        call 5
        local.set 4
        i32.const 2
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
        local.get 4
        local.set 14
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 18297676
        i32.load
        local.set 9
        i32.const 18297676
        i32.const 0
        i32.store
        local.get 9
        i32.const 1
        i32.eq
        local.tee 9
        if  ;; label = @3
          call 9
          local.set 6
          local.get 5
          call 22239
          local.get 6
          call 12
          unreachable
        end
        local.get 6
        local.get 14
        i32.store offset=16
        i32.const 18297676
        i32.const 0
        i32.store
      end
      global.get 2
      i32.eqz
      local.get 7
      i32.const 3
      i32.eq
      i32.or
      if  ;; label = @2
        i32.const 29
        i32.const 24
        call 6
        local.set 4
        i32.const 3
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
        local.get 4
        local.set 9
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 18297676
        i32.load
        local.set 5
        i32.const 18297676
        i32.const 0
        i32.store
        local.get 5
        i32.const 1
        i32.ne
        local.set 5
      end
      block  ;; label = @2
        block  ;; label = @3
          block  ;; label = @4
            block  ;; label = @5
              local.get 5
              global.get 2
              i32.const 2
              i32.eq
              i32.or
              if  ;; label = @6
                global.get 2
                i32.eqz
                if  ;; label = @7
                  i32.const 18297676
                  i32.const 0
                  i32.store
                end
                global.get 2
                i32.eqz
                local.get 7
                i32.const 4
                i32.eq
                i32.or
                if  ;; label = @7
                  i32.const 2284
                  local.get 9
                  i32.const 0
                  i32.const 0
                  call 5
                  local.set 4
                  i32.const 4
                  global.get 2
                  i32.const 1
                  i32.eq
                  br_if 6 (;@1;)
                  drop
                  local.get 4
                  local.set 5
                end
                global.get 2
                i32.eqz
                if  ;; label = @7
                  i32.const 18297676
                  i32.load
                  local.set 13
                  i32.const 18297676
                  i32.const 0
                  i32.store
                  local.get 13
                  i32.const 1
                  i32.eq
                  local.tee 13
                  if  ;; label = @8
                    call 9
                    local.set 5
                    local.get 9
                    call 22239
                    br 5 (;@3;)
                  end
                  local.get 6
                  local.get 5
                  i32.store offset=12
                  local.get 5
                  local.get 12
                  i32.store offset=12
                  local.get 5
                  local.get 10
                  i32.store offset=16
                  local.get 5
                  i32.load offset=4
                  local.tee 9
                  i32.const -4
                  i32.and
                  local.set 12
                  local.get 8
                  i32.const 2147483639
                  i32.ge_u
                  local.set 10
                  local.get 9
                  i32.const 1
                  i32.and
                  if (result i32)  ;; label = @8
                    local.get 12
                    i32.load
                  else
                    local.get 12
                  end
                  local.set 12
                end
                local.get 10
                global.get 2
                i32.const 2
                i32.eq
                i32.or
                if  ;; label = @7
                  global.get 2
                  i32.eqz
                  if  ;; label = @8
                    i32.const 18297676
                    i32.const 0
                    i32.store
                  end
                  global.get 2
                  i32.eqz
                  local.get 7
                  i32.const 5
                  i32.eq
                  i32.or
                  if  ;; label = @8
                    i32.const 112
                    call 11
                    i32.const 5
                    global.get 2
                    i32.const 1
                    i32.eq
                    br_if 7 (;@1;)
                    drop
                  end
                  global.get 2
                  i32.eqz
                  if  ;; label = @8
                    i32.const 18297676
                    i32.load
                    local.set 5
                    i32.const 18297676
                    i32.const 0
                    i32.store
                    local.get 5
                    i32.const 1
                    i32.eq
                    local.tee 0
                    br_if 3 (;@5;)
                    unreachable
                  end
                end
                local.get 10
                local.get 8
                i32.const 10
                i32.le_u
                global.get 2
                select
                local.set 10
                block  ;; label = @7
                  global.get 2
                  i32.eqz
                  if  ;; label = @8
                    local.get 10
                    if  ;; label = @9
                      local.get 6
                      local.get 8
                      i32.store8 offset=31
                      local.get 6
                      i32.const 20
                      i32.add
                      local.set 9
                      br 2 (;@7;)
                    end
                    i32.const 18297676
                    i32.const 0
                    i32.store
                    local.get 8
                    i32.const 2147483640
                    i32.and
                    local.tee 10
                    i32.const 8
                    i32.add
                    local.set 13
                  end
                  global.get 2
                  i32.eqz
                  local.get 7
                  i32.const 6
                  i32.eq
                  i32.or
                  if  ;; label = @8
                    i32.const 29
                    local.get 13
                    call 6
                    local.set 4
                    i32.const 6
                    global.get 2
                    i32.const 1
                    i32.eq
                    br_if 7 (;@1;)
                    drop
                    local.get 4
                    local.set 9
                  end
                  global.get 2
                  i32.eqz
                  if  ;; label = @8
                    i32.const 18297676
                    i32.load
                    local.set 10
                    i32.const 18297676
                    i32.const 0
                    i32.store
                    local.get 10
                    i32.const 1
                    i32.eq
                    br_if 3 (;@5;)
                    local.get 6
                    local.get 8
                    i32.store offset=24
                    local.get 6
                    local.get 9
                    i32.store offset=20
                    local.get 6
                    local.get 13
                    i32.const -2147483648
                    i32.or
                    local.tee 10
                    i32.store offset=28
                  end
                end
                global.get 2
                i32.eqz
                if  ;; label = @7
                  local.get 5
                  i32.const 8
                  i32.add
                  local.set 10
                  local.get 8
                  if  ;; label = @8
                    local.get 9
                    local.get 2
                    local.get 8
                    memory.copy
                  end
                  local.get 8
                  local.get 9
                  i32.add
                  i32.const 0
                  i32.store8
                  i32.const 18297676
                  i32.const 0
                  i32.store
                  local.get 6
                  i32.const 20
                  i32.add
                  local.set 8
                end
                global.get 2
                i32.eqz
                local.get 7
                i32.const 7
                i32.eq
                i32.or
                if  ;; label = @7
                  i32.const 2285
                  local.get 10
                  local.get 8
                  local.get 12
                  call 4
                  i32.const 7
                  global.get 2
                  i32.const 1
                  i32.eq
                  br_if 6 (;@1;)
                  drop
                end
                global.get 2
                if (result i32)  ;; label = @7
                  local.get 8
                else
                  i32.const 18297676
                  i32.load
                  local.set 8
                  i32.const 18297676
                  i32.const 0
                  i32.store
                  local.get 8
                  i32.const 1
                  i32.ne
                end
                global.get 2
                i32.const 2
                i32.eq
                i32.or
                if  ;; label = @7
                  global.get 2
                  i32.eqz
                  if  ;; label = @8
                    local.get 6
                    i32.load8_s offset=31
                    i32.const 0
                    i32.lt_s
                    if  ;; label = @9
                      local.get 6
                      i32.load offset=28
                      drop
                      local.get 6
                      i32.load offset=20
                      call 22239
                    end
                    local.get 6
                    i32.const 0
                    i32.store offset=12
                    i32.const 18297676
                    i32.const 0
                    i32.store
                  end
                  global.get 2
                  i32.eqz
                  local.get 7
                  i32.const 8
                  i32.eq
                  i32.or
                  if  ;; label = @8
                    i32.const 2286
                    local.get 14
                    local.get 5
                    call 0
                    i32.const 8
                    global.get 2
                    i32.const 1
                    i32.eq
                    br_if 7 (;@1;)
                    drop
                  end
                  global.get 2
                  i32.eqz
                  if  ;; label = @8
                    i32.const 18297676
                    i32.load
                    local.set 5
                    i32.const 18297676
                    i32.const 0
                    i32.store
                    local.get 5
                    i32.const 1
                    i32.eq
                    br_if 3 (;@5;)
                    local.get 6
                    i32.const 32
                    i32.add
                    global.set 0
                    br 6 (;@2;)
                  end
                end
                global.get 2
                i32.eqz
                if  ;; label = @7
                  call 9
                  local.set 5
                  local.get 6
                  i32.load8_s offset=31
                  i32.const 0
                  i32.ge_s
                  local.tee 0
                  br_if 3 (;@4;)
                  local.get 6
                  i32.load offset=28
                  drop
                  local.get 6
                  i32.load offset=20
                  local.tee 0
                  call 22239
                  br 3 (;@4;)
                end
              end
              global.get 2
              i32.eqz
              if  ;; label = @6
                call 9
                local.set 5
                br 3 (;@3;)
              end
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              call 9
              local.set 5
            end
          end
          global.get 2
          i32.eqz
          if  ;; label = @4
            local.get 6
            i32.const 12
            i32.add
            local.tee 1
            i32.load
            local.set 0
            local.get 1
            i32.const 0
            i32.store
          end
          local.get 0
          global.get 2
          i32.const 2
          i32.eq
          i32.or
          if  ;; label = @4
            global.get 2
            i32.eqz
            local.get 7
            i32.const 9
            i32.eq
            i32.or
            if  ;; label = @5
              local.get 0
              call 18551
              local.set 4
              i32.const 9
              global.get 2
              i32.const 1
              i32.eq
              br_if 4 (;@1;)
              drop
              local.get 4
              local.set 0
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              local.get 0
              call 22239
            end
          end
        end
        local.get 0
        local.get 6
        i32.const 16
        i32.add
        global.get 2
        select
        local.set 0
        global.get 2
        i32.eqz
        local.get 7
        i32.const 10
        i32.eq
        i32.or
        if  ;; label = @3
          local.get 0
          call 1885
          i32.const 10
          global.get 2
          i32.const 1
          i32.eq
          br_if 2 (;@1;)
          drop
        end
        global.get 2
        i32.eqz
        if  ;; label = @3
          local.get 5
          call 12
          unreachable
        end
      end
      global.get 2
      i32.eqz
      local.get 7
      i32.const 11
      i32.eq
      i32.or
      if  ;; label = @2
        local.get 15
        local.get 14
        call 1911
        i32.const 11
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 18297676
        i32.const 0
        i32.store
      end
      global.get 2
      i32.eqz
      local.get 7
      i32.const 12
      i32.eq
      i32.or
      if  ;; label = @2
        i32.const 2038
        local.get 0
        local.get 1
        local.get 2
        local.get 3
        call 24
        local.set 4
        i32.const 12
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
        local.get 4
        local.set 3
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 18297676
        i32.load
        local.set 2
        i32.const 18297676
        i32.const 0
        i32.store
        local.get 2
        i32.const 1
        i32.eq
        local.set 0
      end
      block  ;; label = @2
        block  ;; label = @3
          global.get 2
          i32.eqz
          if  ;; label = @4
            local.get 0
            br_if 1 (;@3;)
            local.get 3
            i32.const 0
            i32.ge_s
            local.set 0
          end
          block  ;; label = @4
            local.get 0
            global.get 2
            i32.const 2
            i32.eq
            i32.or
            if  ;; label = @5
              global.get 2
              i32.eqz
              if  ;; label = @6
                i32.const 18297676
                i32.const 0
                i32.store
              end
              global.get 2
              i32.eqz
              local.get 7
              i32.const 13
              i32.eq
              i32.or
              if  ;; label = @6
                i32.const 2039
                local.get 3
                call 6
                local.set 4
                i32.const 13
                global.get 2
                i32.const 1
                i32.eq
                br_if 5 (;@1;)
                drop
                local.get 4
                local.set 2
              end
              global.get 2
              i32.eqz
              if  ;; label = @6
                i32.const 18297676
                i32.load
                local.set 1
                i32.const 18297676
                i32.const 0
                i32.store
                local.get 1
                i32.const 1
                i32.ne
                local.tee 0
                br_if 2 (;@4;)
                br 3 (;@3;)
              end
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              i32.const 18297676
              i32.const 0
              i32.store
            end
            global.get 2
            i32.eqz
            local.get 7
            i32.const 14
            i32.eq
            i32.or
            if  ;; label = @5
              i32.const 2039
              local.get 3
              call 6
              local.set 4
              i32.const 14
              global.get 2
              i32.const 1
              i32.eq
              br_if 4 (;@1;)
              drop
              local.get 4
              local.set 2
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              i32.const 18297676
              i32.load
              local.set 1
              i32.const 18297676
              i32.const 0
              i32.store
              local.get 1
              i32.const 1
              i32.eq
              local.tee 0
              br_if 2 (;@3;)
              local.get 11
              local.get 2
              i32.store offset=28
              i32.const 18297676
              i32.const 0
              i32.store
            end
            global.get 2
            i32.eqz
            local.get 7
            i32.const 15
            i32.eq
            i32.or
            if  ;; label = @5
              i32.const 2015
              call 11
              i32.const 15
              global.get 2
              i32.const 1
              i32.eq
              br_if 4 (;@1;)
              drop
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              i32.const 18297676
              i32.load
              local.set 1
              i32.const 18297676
              i32.const 0
              i32.store
              local.get 1
              i32.const 1
              i32.ne
              local.set 0
            end
            local.get 0
            global.get 2
            i32.const 2
            i32.eq
            i32.or
            if  ;; label = @5
              global.get 2
              i32.eqz
              if  ;; label = @6
                i32.const 12158644
                i32.load8_u
                i32.const 1
                i32.ne
                local.tee 0
                br_if 2 (;@4;)
                i32.const 18297676
                i32.const 0
                i32.store
                local.get 11
                i32.const 0
                i32.store offset=28
              end
              global.get 2
              i32.eqz
              local.get 7
              i32.const 16
              i32.eq
              i32.or
              if  ;; label = @6
                i32.const 2040
                local.get 2
                i32.const 12158596
                call 13
                local.set 4
                i32.const 16
                global.get 2
                i32.const 1
                i32.eq
                br_if 5 (;@1;)
                drop
                local.get 4
                local.set 2
              end
              global.get 2
              i32.eqz
              if  ;; label = @6
                i32.const 18297676
                i32.load
                local.set 1
                i32.const 18297676
                i32.const 0
                i32.store
                local.get 1
                i32.const 1
                i32.ne
                local.tee 0
                br_if 2 (;@4;)
              end
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              call 9
              local.set 3
              local.get 11
              i32.const 28
              i32.add
              local.set 0
            end
            global.get 2
            i32.eqz
            local.get 7
            i32.const 17
            i32.eq
            i32.or
            if  ;; label = @5
              local.get 0
              call 1696
              i32.const 17
              global.get 2
              i32.const 1
              i32.eq
              br_if 4 (;@1;)
              drop
            end
            global.get 2
            i32.eqz
            br_if 2 (;@2;)
          end
          global.get 2
          i32.eqz
          if  ;; label = @4
            i32.const 18297676
            i32.const 0
            i32.store
            local.get 11
            i32.const 8
            i32.add
            local.set 0
          end
          global.get 2
          i32.eqz
          local.get 7
          i32.const 18
          i32.eq
          i32.or
          if  ;; label = @4
            i32.const 2012
            local.get 0
            local.get 2
            call 0
            i32.const 18
            global.get 2
            i32.const 1
            i32.eq
            br_if 3 (;@1;)
            drop
          end
          global.get 2
          i32.eqz
          if  ;; label = @4
            i32.const 18297676
            i32.load
            local.set 2
            i32.const 18297676
            i32.const 0
            i32.store
            local.get 2
            i32.const 1
            i32.eq
            local.tee 0
            br_if 1 (;@3;)
            local.get 11
            i32.const 8
            i32.add
            local.set 0
          end
          global.get 2
          i32.eqz
          local.get 7
          i32.const 19
          i32.eq
          i32.or
          if  ;; label = @4
            local.get 0
            call 1906
            i32.const 19
            global.get 2
            i32.const 1
            i32.eq
            br_if 3 (;@1;)
            drop
          end
          global.get 2
          i32.eqz
          if  ;; label = @4
            local.get 11
            i32.const 32
            i32.add
            global.set 0
            local.get 3
            return
          end
        end
        global.get 2
        i32.eqz
        if  ;; label = @3
          call 9
          local.set 3
        end
      end
      local.get 0
      local.get 11
      i32.const 8
      i32.add
      global.get 2
      select
      local.set 0
      global.get 2
      i32.eqz
      local.get 7
      i32.const 20
      i32.eq
      i32.or
      if  ;; label = @2
        local.get 0
        call 1906
        i32.const 20
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        local.get 3
        call 12
        unreachable
      end
      unreachable
    end
    local.set 4
    global.get 3
    i32.load
    local.get 4
    i32.store
    global.get 3
    global.get 3
    i32.load
    i32.const 4
    i32.add
    i32.store
    global.get 3
    i32.load
    local.tee 4
    local.get 0
    i32.store
    local.get 4
    local.get 1
    i32.store offset=4
    local.get 4
    local.get 2
    i32.store offset=8
    local.get 4
    local.get 3
    i32.store offset=12
    local.get 4
    local.get 5
    i32.store offset=16
    local.get 4
    local.get 6
    i32.store offset=20
    local.get 4
    local.get 8
    i32.store offset=24
    local.get 4
    local.get 10
    i32.store offset=28
    local.get 4
    local.get 9
    i32.store offset=32
    local.get 4
    local.get 11
    i32.store offset=36
    local.get 4
    local.get 12
    i32.store offset=40
    local.get 4
    local.get 13
    i32.store offset=44
    local.get 4
    local.get 14
    i32.store offset=48
    local.get 4
    local.get 15
    i32.store offset=52
    global.get 3
    global.get 3
    i32.load
    i32.const 56
    i32.add
    i32.store
    i32.const 0)
;; Exports: CEE_DisposeFeature
  (func (;1697;) (type 0) (param i32)
    (local i32 i32 i32 i32 i32 i32 i32 i32)
    global.get 2
    i32.const 2
    i32.eq
    if  ;; label = @1
      global.get 3
      global.get 3
      i32.load
      i32.const 28
      i32.sub
      i32.store
      global.get 3
      i32.load
      local.tee 1
      i32.load
      local.set 0
      local.get 1
      i32.load offset=8
      local.set 3
      local.get 1
      i32.load offset=12
      local.set 5
      local.get 1
      i32.load offset=16
      local.set 7
      local.get 1
      i32.load offset=20
      local.set 6
      local.get 1
      i32.load offset=24
      local.set 8
      local.get 1
      i32.load offset=4
      local.set 2
    end
    block (result i32)  ;; label = @1
      global.get 2
      i32.const 2
      i32.eq
      if  ;; label = @2
        global.get 3
        global.get 3
        i32.load
        i32.const 4
        i32.sub
        i32.store
        global.get 3
        i32.load
        i32.load
        local.set 4
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        global.get 0
        i32.const 32
        i32.sub
        local.tee 7
        global.set 0
        global.get 0
        local.tee 3
        i32.const 16
        i32.sub
        local.tee 5
        global.set 0
        local.get 7
        i32.const 12
        i32.add
        local.set 8
      end
      global.get 2
      i32.eqz
      local.get 4
      i32.eqz
      i32.or
      if  ;; label = @2
        i32.const 24
        call 22866
        local.set 1
        i32.const 0
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
        local.get 1
        local.set 2
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 18297676
        i32.const 0
        i32.store
      end
      global.get 2
      i32.eqz
      local.get 4
      i32.const 1
      i32.eq
      i32.or
      if  ;; label = @2
        i32.const 2279
        local.get 2
        i32.const 0
        i32.const 0
        call 5
        local.set 1
        i32.const 1
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
        local.get 1
        local.set 3
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 18297676
        i32.load
        local.set 6
        i32.const 18297676
        i32.const 0
        i32.store
        local.get 6
        i32.const 1
        i32.eq
        local.tee 6
        if  ;; label = @3
          call 9
          local.set 5
          local.get 2
          call 22239
          local.get 5
          call 12
          unreachable
        end
        local.get 5
        local.get 3
        i32.store offset=12
        i32.const 18297676
        i32.const 0
        i32.store
      end
      global.get 2
      i32.eqz
      local.get 4
      i32.const 2
      i32.eq
      i32.or
      if  ;; label = @2
        i32.const 29
        i32.const 16
        call 6
        local.set 1
        i32.const 2
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
        local.get 1
        local.set 6
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 18297676
        i32.load
        local.set 2
        i32.const 18297676
        i32.const 0
        i32.store
        local.get 2
        i32.const 1
        i32.ne
        local.set 2
      end
      block  ;; label = @2
        block  ;; label = @3
          block  ;; label = @4
            local.get 2
            global.get 2
            i32.const 2
            i32.eq
            i32.or
            if  ;; label = @5
              global.get 2
              i32.eqz
              if  ;; label = @6
                i32.const 18297676
                i32.const 0
                i32.store
              end
              global.get 2
              i32.eqz
              local.get 4
              i32.const 3
              i32.eq
              i32.or
              if  ;; label = @6
                i32.const 2289
                local.get 6
                i32.const 0
                i32.const 0
                call 5
                local.set 1
                i32.const 3
                global.get 2
                i32.const 1
                i32.eq
                br_if 5 (;@1;)
                drop
                local.get 1
                local.set 2
              end
              global.get 2
              i32.eqz
              if  ;; label = @6
                i32.const 18297676
                i32.load
                local.set 1
                i32.const 18297676
                i32.const 0
                i32.store
                local.get 1
                i32.const 1
                i32.eq
                if  ;; label = @7
                  call 9
                  local.set 3
                  local.get 6
                  call 22239
                  br 4 (;@3;)
                end
                local.get 2
                local.get 0
                i32.store offset=8
                i32.const 18297676
                i32.const 0
                i32.store
                local.get 5
                i32.const 0
                i32.store offset=8
              end
              global.get 2
              i32.eqz
              local.get 4
              i32.const 4
              i32.eq
              i32.or
              if  ;; label = @6
                i32.const 2290
                local.get 3
                local.get 2
                call 0
                i32.const 4
                global.get 2
                i32.const 1
                i32.eq
                br_if 5 (;@1;)
                drop
              end
              global.get 2
              i32.eqz
              if  ;; label = @6
                i32.const 18297676
                i32.load
                local.set 2
                i32.const 18297676
                i32.const 0
                i32.store
                local.get 2
                i32.const 1
                i32.eq
                local.tee 2
                br_if 2 (;@4;)
                local.get 5
                i32.const 16
                i32.add
                local.tee 2
                global.set 0
                br 4 (;@2;)
              end
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              call 9
              local.set 3
              br 2 (;@3;)
            end
          end
          global.get 2
          i32.eqz
          if  ;; label = @4
            call 9
            local.set 3
            local.get 5
            i32.const 8
            i32.add
            local.tee 2
            i32.load
            local.set 0
            local.get 2
            i32.const 0
            i32.store
          end
          local.get 0
          global.get 2
          i32.const 2
          i32.eq
          i32.or
          if  ;; label = @4
            global.get 2
            i32.eqz
            local.get 4
            i32.const 5
            i32.eq
            i32.or
            if  ;; label = @5
              local.get 0
              call 18563
              local.set 1
              i32.const 5
              global.get 2
              i32.const 1
              i32.eq
              br_if 4 (;@1;)
              drop
              local.get 1
              local.set 0
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              local.get 0
              call 22239
            end
          end
        end
        local.get 0
        local.get 5
        i32.const 12
        i32.add
        global.get 2
        select
        local.set 0
        global.get 2
        i32.eqz
        local.get 4
        i32.const 6
        i32.eq
        i32.or
        if  ;; label = @3
          local.get 0
          call 1885
          i32.const 6
          global.get 2
          i32.const 1
          i32.eq
          br_if 2 (;@1;)
          drop
        end
        global.get 2
        i32.eqz
        if  ;; label = @3
          local.get 3
          call 12
          unreachable
        end
      end
      global.get 2
      i32.eqz
      local.get 4
      i32.const 7
      i32.eq
      i32.or
      if  ;; label = @2
        local.get 8
        local.get 3
        call 1911
        i32.const 7
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 18297676
        i32.const 0
        i32.store
        i32.const 18297676
        i32.load
        local.set 2
        i32.const 18297676
        i32.const 0
        i32.store
        local.get 2
        i32.const 1
        i32.eq
        local.set 3
      end
      block  ;; label = @2
        global.get 2
        i32.eqz
        if  ;; label = @3
          local.get 3
          br_if 1 (;@2;)
          i32.const 18297676
          i32.const 0
          i32.store
        end
        global.get 2
        i32.eqz
        local.get 4
        i32.const 8
        i32.eq
        i32.or
        if  ;; label = @3
          i32.const 2041
          i32.const 12157936
          local.get 0
          call 0
          i32.const 8
          global.get 2
          i32.const 1
          i32.eq
          br_if 2 (;@1;)
          drop
        end
        global.get 2
        i32.eqz
        if  ;; label = @3
          i32.const 18297676
          i32.load
          local.set 0
          i32.const 18297676
          i32.const 0
          i32.store
          local.get 0
          i32.const 1
          i32.eq
          local.tee 0
          br_if 1 (;@2;)
          i32.const 18297676
          i32.const 0
          i32.store
        end
        global.get 2
        i32.eqz
        local.get 4
        i32.const 9
        i32.eq
        i32.or
        if  ;; label = @3
          i32.const 2042
          call 21
          local.set 1
          i32.const 9
          global.get 2
          i32.const 1
          i32.eq
          br_if 2 (;@1;)
          drop
          local.get 1
          local.set 2
        end
        global.get 2
        i32.eqz
        if  ;; label = @3
          i32.const 18297676
          i32.load
          local.set 0
          i32.const 18297676
          i32.const 0
          i32.store
          local.get 0
          i32.const 1
          i32.eq
          local.tee 0
          br_if 1 (;@2;)
          i32.const 18297676
          i32.const 0
          i32.store
          local.get 7
          i32.const 12
          i32.add
          local.set 0
        end
        global.get 2
        i32.eqz
        local.get 4
        i32.const 10
        i32.eq
        i32.or
        if  ;; label = @3
          i32.const 2012
          local.get 0
          local.get 2
          call 0
          i32.const 10
          global.get 2
          i32.const 1
          i32.eq
          br_if 2 (;@1;)
          drop
        end
        global.get 2
        i32.eqz
        if  ;; label = @3
          i32.const 18297676
          i32.load
          local.set 0
          i32.const 18297676
          i32.const 0
          i32.store
          local.get 0
          i32.const 1
          i32.eq
          local.tee 0
          br_if 1 (;@2;)
          local.get 7
          i32.const 12
          i32.add
          local.set 0
        end
        global.get 2
        i32.eqz
        local.get 4
        i32.const 11
        i32.eq
        i32.or
        if  ;; label = @3
          local.get 0
          call 1906
          i32.const 11
          global.get 2
          i32.const 1
          i32.eq
          br_if 2 (;@1;)
          drop
        end
        global.get 2
        i32.eqz
        if  ;; label = @3
          local.get 7
          i32.const 32
          i32.add
          global.set 0
          return
        end
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        local.get 7
        i32.const 12
        i32.add
        local.set 3
        call 9
        local.set 0
      end
      global.get 2
      i32.eqz
      local.get 4
      i32.const 12
      i32.eq
      i32.or
      if  ;; label = @2
        local.get 3
        call 1906
        i32.const 12
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        local.get 0
        call 12
        unreachable
      end
      return
    end
    local.set 1
    global.get 3
    i32.load
    local.get 1
    i32.store
    global.get 3
    global.get 3
    i32.load
    i32.const 4
    i32.add
    i32.store
    global.get 3
    i32.load
    local.tee 1
    local.get 0
    i32.store
    local.get 1
    local.get 2
    i32.store offset=4
    local.get 1
    local.get 3
    i32.store offset=8
    local.get 1
    local.get 5
    i32.store offset=12
    local.get 1
    local.get 7
    i32.store offset=16
    local.get 1
    local.get 6
    i32.store offset=20
    local.get 1
    local.get 8
    i32.store offset=24
    global.get 3
    global.get 3
    i32.load
    i32.const 28
    i32.add
    i32.store)
;; Exports: CEE_Run
  (func (;1699;) (type 3) (param i32 i32) (result i32)
    (local i32 i32 i32 i32 i32 i32 i32 i32)
    global.get 2
    i32.const 2
    i32.eq
    if  ;; label = @1
      global.get 3
      global.get 3
      i32.load
      i32.const 32
      i32.sub
      i32.store
      global.get 3
      i32.load
      local.tee 4
      i32.load
      local.set 0
      local.get 4
      i32.load offset=8
      local.set 2
      local.get 4
      i32.load offset=12
      local.set 3
      local.get 4
      i32.load offset=16
      local.set 6
      local.get 4
      i32.load offset=20
      local.set 7
      local.get 4
      i32.load offset=24
      local.set 8
      local.get 4
      i32.load offset=28
      local.set 9
      local.get 4
      i32.load offset=4
      local.set 1
    end
    block (result i32)  ;; label = @1
      global.get 2
      i32.const 2
      i32.eq
      if  ;; label = @2
        global.get 3
        global.get 3
        i32.load
        i32.const 4
        i32.sub
        i32.store
        global.get 3
        i32.load
        i32.load
        local.set 5
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        global.get 0
        local.tee 2
        i32.const 32
        i32.sub
        local.tee 6
        global.set 0
      end
      global.get 2
      i32.eqz
      local.get 5
      i32.eqz
      i32.or
      if  ;; label = @2
        call 1943
        i32.const 0
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 12158592
        call 1695
        global.get 0
        local.tee 2
        i32.const 16
        i32.sub
        local.tee 7
        global.set 0
        local.get 6
        i32.const 12
        i32.add
        local.set 9
      end
      global.get 2
      i32.eqz
      local.get 5
      i32.const 1
      i32.eq
      i32.or
      if  ;; label = @2
        i32.const 24
        call 22866
        local.set 4
        i32.const 1
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
        local.get 4
        local.set 3
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 18297676
        i32.const 0
        i32.store
      end
      global.get 2
      i32.eqz
      local.get 5
      i32.const 2
      i32.eq
      i32.or
      if  ;; label = @2
        i32.const 2279
        local.get 3
        i32.const 0
        i32.const 0
        call 5
        local.set 4
        i32.const 2
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
        local.get 4
        local.set 2
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 18297676
        i32.load
        local.set 8
        i32.const 18297676
        i32.const 0
        i32.store
        local.get 8
        i32.const 1
        i32.eq
        local.tee 8
        if  ;; label = @3
          call 9
          local.set 7
          local.get 3
          call 22239
          local.get 7
          call 12
          unreachable
        end
        local.get 7
        local.get 2
        i32.store offset=12
        i32.const 18297676
        i32.const 0
        i32.store
      end
      global.get 2
      i32.eqz
      local.get 5
      i32.const 3
      i32.eq
      i32.or
      if  ;; label = @2
        i32.const 29
        i32.const 20
        call 6
        local.set 4
        i32.const 3
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
        local.get 4
        local.set 8
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        i32.const 18297676
        i32.load
        local.set 3
        i32.const 18297676
        i32.const 0
        i32.store
        local.get 3
        i32.const 1
        i32.ne
        local.set 3
      end
      block  ;; label = @2
        block  ;; label = @3
          block  ;; label = @4
            local.get 3
            global.get 2
            i32.const 2
            i32.eq
            i32.or
            if  ;; label = @5
              global.get 2
              i32.eqz
              if  ;; label = @6
                i32.const 18297676
                i32.const 0
                i32.store
              end
              global.get 2
              i32.eqz
              local.get 5
              i32.const 4
              i32.eq
              i32.or
              if  ;; label = @6
                i32.const 2291
                local.get 8
                i32.const 0
                i32.const 0
                call 5
                local.set 4
                i32.const 4
                global.get 2
                i32.const 1
                i32.eq
                br_if 5 (;@1;)
                drop
                local.get 4
                local.set 3
              end
              global.get 2
              i32.eqz
              if  ;; label = @6
                i32.const 18297676
                i32.load
                local.set 4
                i32.const 18297676
                i32.const 0
                i32.store
                local.get 4
                i32.const 1
                i32.eq
                if  ;; label = @7
                  call 9
                  local.set 2
                  local.get 8
                  call 22239
                  br 4 (;@3;)
                end
                local.get 3
                local.get 1
                i32.store offset=12
                local.get 3
                local.get 0
                i32.store offset=8
                i32.const 18297676
                i32.const 0
                i32.store
                local.get 7
                i32.const 0
                i32.store offset=8
              end
              global.get 2
              i32.eqz
              local.get 5
              i32.const 5
              i32.eq
              i32.or
              if  ;; label = @6
                i32.const 2292
                local.get 2
                local.get 3
                call 0
                i32.const 5
                global.get 2
                i32.const 1
                i32.eq
                br_if 5 (;@1;)
                drop
              end
              global.get 2
              i32.eqz
              if  ;; label = @6
                i32.const 18297676
                i32.load
                local.set 3
                i32.const 18297676
                i32.const 0
                i32.store
                local.get 3
                i32.const 1
                i32.eq
                local.tee 3
                br_if 2 (;@4;)
                local.get 7
                i32.const 16
                i32.add
                local.tee 3
                global.set 0
                br 4 (;@2;)
              end
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              call 9
              local.set 2
              br 2 (;@3;)
            end
          end
          global.get 2
          i32.eqz
          if  ;; label = @4
            call 9
            local.set 2
            local.get 7
            i32.const 8
            i32.add
            local.tee 1
            i32.load
            local.set 0
            local.get 1
            i32.const 0
            i32.store
          end
          local.get 0
          global.get 2
          i32.const 2
          i32.eq
          i32.or
          if  ;; label = @4
            global.get 2
            i32.eqz
            local.get 5
            i32.const 6
            i32.eq
            i32.or
            if  ;; label = @5
              local.get 0
              call 18528
              local.set 4
              i32.const 6
              global.get 2
              i32.const 1
              i32.eq
              br_if 4 (;@1;)
              drop
              local.get 4
              local.set 0
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              local.get 0
              call 22239
            end
          end
        end
        local.get 0
        local.get 7
        i32.const 12
        i32.add
        global.get 2
        select
        local.set 0
        global.get 2
        i32.eqz
        local.get 5
        i32.const 7
        i32.eq
        i32.or
        if  ;; label = @3
          local.get 0
          call 1885
          i32.const 7
          global.get 2
          i32.const 1
          i32.eq
          br_if 2 (;@1;)
          drop
        end
        global.get 2
        i32.eqz
        if  ;; label = @3
          local.get 2
          call 12
          unreachable
        end
      end
      global.get 2
      i32.eqz
      local.get 5
      i32.const 8
      i32.eq
      i32.or
      if  ;; label = @2
        local.get 9
        local.get 2
        call 1911
        i32.const 8
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
      end
      local.get 2
      local.get 1
      i32.eqz
      global.get 2
      select
      local.set 2
      block  ;; label = @2
        block  ;; label = @3
          block  ;; label = @4
            block  ;; label = @5
              block  ;; label = @6
                block  ;; label = @7
                  block  ;; label = @8
                    block  ;; label = @9
                      global.get 2
                      i32.eqz
                      if  ;; label = @10
                        local.get 2
                        br_if 1 (;@9;)
                        i32.const 18297676
                        i32.const 0
                        i32.store
                        i32.const 18297676
                        i32.load
                        local.set 3
                        i32.const 18297676
                        i32.const 0
                        i32.store
                        local.get 3
                        i32.const 1
                        i32.eq
                        br_if 6 (;@4;)
                        i32.const 18297676
                        i32.const 0
                        i32.store
                        local.get 6
                        i32.const 4
                        i32.add
                        local.set 2
                      end
                      global.get 2
                      i32.eqz
                      local.get 5
                      i32.const 9
                      i32.eq
                      i32.or
                      if  ;; label = @10
                        i32.const 2043
                        local.get 2
                        i32.const 12157936
                        local.get 0
                        call 4
                        i32.const 9
                        global.get 2
                        i32.const 1
                        i32.eq
                        br_if 9 (;@1;)
                        drop
                      end
                      global.get 2
                      i32.eqz
                      if  ;; label = @10
                        i32.const 18297676
                        i32.load
                        local.set 3
                        i32.const 18297676
                        i32.const 0
                        i32.store
                        local.get 3
                        i32.const 1
                        i32.eq
                        br_if 6 (;@4;)
                        local.get 6
                        i32.load offset=4
                        local.tee 7
                        i32.eqz
                        local.set 2
                      end
                      block  ;; label = @10
                        global.get 2
                        i32.eqz
                        if  ;; label = @11
                          local.get 2
                          br_if 1 (;@10;)
                          i32.const 18297676
                          i32.const 0
                          i32.store
                          local.get 6
                          i32.const 12
                          i32.add
                          call 1909
                          local.set 3
                          i32.const 18297676
                          i32.load
                          local.set 2
                          i32.const 18297676
                          i32.const 0
                          i32.store
                          local.get 2
                          i32.const 1
                          i32.ne
                          local.set 2
                        end
                        local.get 2
                        global.get 2
                        i32.const 2
                        i32.eq
                        i32.or
                        if  ;; label = @11
                          global.get 2
                          i32.eqz
                          if  ;; label = @12
                            i32.const 18297676
                            i32.const 0
                            i32.store
                            local.get 6
                            local.get 3
                            i32.store
                            local.get 6
                            i32.load offset=16
                            local.set 8
                            i32.const 18297676
                            i32.load
                            local.set 2
                            i32.const 18297676
                            i32.const 0
                            i32.store
                            local.get 2
                            i32.const 1
                            i32.eq
                            local.tee 2
                            br_if 4 (;@8;)
                            i32.const 18297676
                            i32.const 0
                            i32.store
                          end
                          global.get 2
                          i32.eqz
                          local.get 5
                          i32.const 10
                          i32.eq
                          i32.or
                          if  ;; label = @12
                            i32.const 2051
                            local.get 7
                            local.get 3
                            local.get 8
                            call 4
                            i32.const 10
                            global.get 2
                            i32.const 1
                            i32.eq
                            br_if 11 (;@1;)
                            drop
                          end
                          global.get 2
                          i32.eqz
                          if  ;; label = @12
                            i32.const 18297676
                            i32.load
                            local.set 3
                            i32.const 18297676
                            i32.const 0
                            i32.store
                            local.get 3
                            i32.const 1
                            i32.ne
                            local.tee 2
                            br_if 2 (;@10;)
                          end
                        end
                        global.get 2
                        i32.eqz
                        if  ;; label = @11
                          call 9
                          local.set 1
                          br 4 (;@7;)
                        end
                      end
                      global.get 2
                      i32.eqz
                      if  ;; label = @10
                        local.get 6
                        i32.load offset=8
                        local.tee 3
                        i32.eqz
                        local.tee 2
                        br_if 1 (;@9;)
                        local.get 3
                        local.get 3
                        i32.load offset=4
                        local.tee 7
                        i32.const 1
                        i32.sub
                        local.tee 2
                        i32.store offset=4
                        local.get 7
                        br_if 1 (;@9;)
                        local.get 3
                        i32.load
                        i32.load offset=8
                        local.set 2
                      end
                      global.get 2
                      i32.eqz
                      local.get 5
                      i32.const 11
                      i32.eq
                      i32.or
                      if  ;; label = @10
                        local.get 3
                        local.get 2
                        call_indirect (type 0)
                        i32.const 11
                        global.get 2
                        i32.const 1
                        i32.eq
                        br_if 9 (;@1;)
                        drop
                      end
                      global.get 2
                      i32.eqz
                      local.get 5
                      i32.const 12
                      i32.eq
                      i32.or
                      if  ;; label = @10
                        local.get 3
                        call 22862
                        i32.const 12
                        global.get 2
                        i32.const 1
                        i32.eq
                        br_if 9 (;@1;)
                        drop
                      end
                    end
                    global.get 2
                    i32.eqz
                    if  ;; label = @9
                      i32.const 18297676
                      i32.const 0
                      i32.store
                    end
                    global.get 2
                    i32.eqz
                    local.get 5
                    i32.const 13
                    i32.eq
                    i32.or
                    if  ;; label = @9
                      i32.const 2052
                      local.get 0
                      local.get 1
                      call 13
                      local.set 4
                      i32.const 13
                      global.get 2
                      i32.const 1
                      i32.eq
                      br_if 8 (;@1;)
                      drop
                      local.get 4
                      local.set 1
                    end
                    global.get 2
                    i32.eqz
                    if  ;; label = @9
                      i32.const 18297676
                      i32.load
                      local.set 0
                      i32.const 18297676
                      i32.const 0
                      i32.store
                      local.get 0
                      i32.const 1
                      i32.eq
                      local.tee 0
                      br_if 6 (;@3;)
                      local.get 1
                      i32.const 0
                      i32.le_s
                      local.tee 0
                      br_if 3 (;@6;)
                      i32.const 18297676
                      i32.const 0
                      i32.store
                    end
                    global.get 2
                    i32.eqz
                    local.get 5
                    i32.const 14
                    i32.eq
                    i32.or
                    if  ;; label = @9
                      i32.const 2053
                      i32.const 1
                      call 6
                      local.set 4
                      i32.const 14
                      global.get 2
                      i32.const 1
                      i32.eq
                      br_if 8 (;@1;)
                      drop
                      local.get 4
                      local.set 0
                    end
                    global.get 2
                    i32.eqz
                    if  ;; label = @9
                      i32.const 18297676
                      i32.load
                      local.set 3
                      i32.const 18297676
                      i32.const 0
                      i32.store
                      local.get 3
                      i32.const 1
                      i32.ne
                      local.tee 2
                      br_if 4 (;@5;)
                      br 6 (;@3;)
                    end
                  end
                  global.get 2
                  i32.eqz
                  if  ;; label = @8
                    call 9
                    local.set 1
                  end
                  global.get 2
                  i32.eqz
                  local.get 5
                  i32.const 15
                  i32.eq
                  i32.or
                  if  ;; label = @8
                    local.get 6
                    call 498
                    i32.const 15
                    global.get 2
                    i32.const 1
                    i32.eq
                    br_if 7 (;@1;)
                    drop
                  end
                end
                local.get 0
                local.get 6
                i32.const 4
                i32.add
                global.get 2
                select
                local.set 0
                global.get 2
                i32.eqz
                local.get 5
                i32.const 16
                i32.eq
                i32.or
                if  ;; label = @7
                  local.get 0
                  call 205
                  i32.const 16
                  global.get 2
                  i32.const 1
                  i32.eq
                  br_if 6 (;@1;)
                  drop
                end
                global.get 2
                i32.eqz
                br_if 4 (;@2;)
              end
              global.get 2
              i32.eqz
              if  ;; label = @6
                i32.const 18297676
                i32.const 0
                i32.store
              end
              global.get 2
              i32.eqz
              local.get 5
              i32.const 17
              i32.eq
              i32.or
              if  ;; label = @6
                i32.const 2053
                local.get 1
                call 6
                local.set 4
                i32.const 17
                global.get 2
                i32.const 1
                i32.eq
                br_if 5 (;@1;)
                drop
                local.get 4
                local.set 0
              end
              global.get 2
              i32.eqz
              if  ;; label = @6
                i32.const 18297676
                i32.load
                local.set 3
                i32.const 18297676
                i32.const 0
                i32.store
                local.get 3
                i32.const 1
                i32.eq
                local.tee 2
                br_if 3 (;@3;)
                local.get 6
                local.get 0
                i32.store offset=4
                i32.const 18297676
                i32.const 0
                i32.store
              end
              global.get 2
              i32.eqz
              local.get 5
              i32.const 18
              i32.eq
              i32.or
              if  ;; label = @6
                i32.const 2015
                call 11
                i32.const 18
                global.get 2
                i32.const 1
                i32.eq
                br_if 5 (;@1;)
                drop
              end
              global.get 2
              i32.eqz
              if  ;; label = @6
                i32.const 18297676
                i32.load
                local.set 3
                i32.const 18297676
                i32.const 0
                i32.store
                local.get 3
                i32.const 1
                i32.ne
                local.set 2
              end
              local.get 2
              global.get 2
              i32.const 2
              i32.eq
              i32.or
              if  ;; label = @6
                global.get 2
                i32.eqz
                if  ;; label = @7
                  i32.const 12158644
                  i32.load8_u
                  i32.const 1
                  i32.ne
                  local.tee 2
                  br_if 2 (;@5;)
                  i32.const 18297676
                  i32.const 0
                  i32.store
                  local.get 6
                  i32.const 0
                  i32.store offset=4
                end
                global.get 2
                i32.eqz
                local.get 5
                i32.const 19
                i32.eq
                i32.or
                if  ;; label = @7
                  i32.const 2040
                  local.get 0
                  i32.const 12158596
                  call 13
                  local.set 4
                  i32.const 19
                  global.get 2
                  i32.const 1
                  i32.eq
                  br_if 6 (;@1;)
                  drop
                  local.get 4
                  local.set 0
                end
                global.get 2
                i32.eqz
                if  ;; label = @7
                  i32.const 18297676
                  i32.load
                  local.set 3
                  i32.const 18297676
                  i32.const 0
                  i32.store
                  local.get 3
                  i32.const 1
                  i32.ne
                  local.tee 2
                  br_if 2 (;@5;)
                end
              end
              global.get 2
              i32.eqz
              if  ;; label = @6
                call 9
                local.set 1
                local.get 6
                i32.const 4
                i32.add
                local.set 0
              end
              global.get 2
              i32.eqz
              local.get 5
              i32.const 20
              i32.eq
              i32.or
              if  ;; label = @6
                local.get 0
                call 1696
                i32.const 20
                global.get 2
                i32.const 1
                i32.eq
                br_if 5 (;@1;)
                drop
              end
              global.get 2
              i32.eqz
              br_if 3 (;@2;)
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              i32.const 18297676
              i32.const 0
              i32.store
              local.get 6
              i32.const 12
              i32.add
              local.set 2
            end
            global.get 2
            i32.eqz
            local.get 5
            i32.const 21
            i32.eq
            i32.or
            if  ;; label = @5
              i32.const 2012
              local.get 2
              local.get 0
              call 0
              i32.const 21
              global.get 2
              i32.const 1
              i32.eq
              br_if 4 (;@1;)
              drop
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              i32.const 18297676
              i32.load
              local.set 0
              i32.const 18297676
              i32.const 0
              i32.store
              local.get 0
              i32.const 1
              i32.eq
              local.tee 0
              br_if 2 (;@3;)
              local.get 6
              i32.const 12
              i32.add
              local.set 0
            end
            global.get 2
            i32.eqz
            local.get 5
            i32.const 22
            i32.eq
            i32.or
            if  ;; label = @5
              local.get 0
              call 1906
              i32.const 22
              global.get 2
              i32.const 1
              i32.eq
              br_if 4 (;@1;)
              drop
            end
            global.get 2
            i32.eqz
            if  ;; label = @5
              local.get 6
              i32.const 32
              i32.add
              global.set 0
              local.get 1
              return
            end
          end
          global.get 2
          i32.eqz
          if  ;; label = @4
            call 9
            local.set 1
            br 2 (;@2;)
          end
        end
        global.get 2
        i32.eqz
        if  ;; label = @3
          call 9
          local.set 1
        end
      end
      local.get 0
      local.get 6
      i32.const 12
      i32.add
      global.get 2
      select
      local.set 0
      global.get 2
      i32.eqz
      local.get 5
      i32.const 23
      i32.eq
      i32.or
      if  ;; label = @2
        local.get 0
        call 1906
        i32.const 23
        global.get 2
        i32.const 1
        i32.eq
        br_if 1 (;@1;)
        drop
      end
      global.get 2
      i32.eqz
      if  ;; label = @2
        local.get 1
        call 12
        unreachable
      end
      unreachable
    end
    local.set 4
    global.get 3
    i32.load
    local.get 4
    i32.store
    global.get 3
    global.get 3
    i32.load
    i32.const 4
    i32.add
    i32.store
    global.get 3
    i32.load
    local.tee 4
    local.get 0
    i32.store
    local.get 4
    local.get 1
    i32.store offset=4
    local.get 4
    local.get 2
    i32.store offset=8
    local.get 4
    local.get 3
    i32.store offset=12
    local.get 4
    local.get 6
    i32.store offset=16
    local.get 4
    local.get 7
    i32.store offset=20
    local.get 4
    local.get 8
    i32.store offset=24
    local.get 4
    local.get 9
    i32.store offset=28
    global.get 3
    global.get 3
    i32.load
    i32.const 32
    i32.add
    i32.store
    i32.const 0)
;; Exports: malloc
  (func (;22238;) (type 2) (param i32) (result i32)
    (local i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32)
    global.get 0
    i32.const 16
    i32.sub
    local.tee 10
    global.set 0
    block  ;; label = @1
      block  ;; label = @2
        block  ;; label = @3
          block  ;; label = @4
            block  ;; label = @5
              block  ;; label = @6
                block  ;; label = @7
                  block  ;; label = @8
                    block  ;; label = @9
                      block  ;; label = @10
                        local.get 0
                        i32.const 244
                        i32.le_u
                        if  ;; label = @11
                          i32.const 18297180
                          i32.load
                          local.tee 6
                          i32.const 16
                          local.get 0
                          i32.const 11
                          i32.add
                          i32.const 504
                          i32.and
                          local.get 0
                          i32.const 11
                          i32.lt_u
                          select
                          local.tee 4
                          i32.const 3
                          i32.shr_u
                          local.tee 1
                          i32.shr_u
                          local.tee 0
                          i32.const 3
                          i32.and
                          if  ;; label = @12
                            block  ;; label = @13
                              local.get 0
                              i32.const -1
                              i32.xor
                              i32.const 1
                              i32.and
                              local.get 1
                              i32.add
                              local.tee 2
                              i32.const 3
                              i32.shl
                              local.tee 1
                              i32.const 18297220
                              i32.add
                              local.tee 0
                              local.get 1
                              i32.load offset=18297228
                              local.tee 4
                              i32.load offset=8
                              local.tee 3
                              i32.eq
                              if  ;; label = @14
                                i32.const 18297180
                                local.get 6
                                i32.const -2
                                local.get 2
                                i32.rotl
                                i32.and
                                i32.store
                                br 1 (;@13;)
                              end
                              local.get 3
                              local.get 0
                              i32.store offset=12
                              local.get 0
                              local.get 3
                              i32.store offset=8
                            end
                            local.get 4
                            i32.const 8
                            i32.add
                            local.set 0
                            local.get 4
                            local.get 1
                            i32.const 3
                            i32.or
                            i32.store offset=4
                            local.get 1
                            local.get 4
                            i32.add
                            local.tee 1
                            local.get 1
                            i32.load offset=4
                            i32.const 1
                            i32.or
                            i32.store offset=4
                            br 11 (;@1;)
                          end
                          local.get 4
                          i32.const 18297188
                          i32.load
                          local.tee 8
                          i32.le_u
                          br_if 1 (;@10;)
                          local.get 0
                          if  ;; label = @12
                            block  ;; label = @13
                              local.get 0
                              local.get 1
                              i32.shl
                              i32.const 2
                              local.get 1
                              i32.shl
                              local.tee 0
                              i32.const 0
                              local.get 0
                              i32.sub
                              i32.or
                              i32.and
                              i32.ctz
                              local.tee 5
                              i32.const 3
                              i32.shl
                              local.tee 1
                              i32.const 18297220
                              i32.add
                              local.tee 3
                              local.get 1
                              i32.load offset=18297228
                              local.tee 0
                              i32.load offset=8
                              local.tee 2
                              i32.eq
                              if  ;; label = @14
                                i32.const 18297180
                                local.get 6
                                i32.const -2
                                local.get 5
                                i32.rotl
                                i32.and
                                local.tee 6
                                i32.store
                                br 1 (;@13;)
                              end
                              local.get 2
                              local.get 3
                              i32.store offset=12
                              local.get 3
                              local.get 2
                              i32.store offset=8
                            end
                            local.get 0
                            local.get 4
                            i32.const 3
                            i32.or
                            i32.store offset=4
                            local.get 0
                            local.get 4
                            i32.add
                            local.tee 2
                            local.get 1
                            local.get 4
                            i32.sub
                            local.tee 4
                            i32.const 1
                            i32.or
                            i32.store offset=4
                            local.get 0
                            local.get 1
                            i32.add
                            local.get 4
                            i32.store
                            local.get 8
                            if  ;; label = @13
                              local.get 8
                              i32.const -8
                              i32.and
                              i32.const 18297220
                              i32.add
                              local.set 3
                              i32.const 18297200
                              i32.load
                              local.set 1
                              block (result i32)  ;; label = @14
                                local.get 6
                                i32.const 1
                                local.get 8
                                i32.const 3
                                i32.shr_u
                                i32.shl
                                local.tee 5
                                i32.and
                                i32.eqz
                                if  ;; label = @15
                                  i32.const 18297180
                                  local.get 5
                                  local.get 6
                                  i32.or
                                  i32.store
                                  local.get 3
                                  br 1 (;@14;)
                                end
                                local.get 3
                                i32.load offset=8
                              end
                              local.set 5
                              local.get 3
                              local.get 1
                              i32.store offset=8
                              local.get 5
                              local.get 1
                              i32.store offset=12
                              local.get 1
                              local.get 3
                              i32.store offset=12
                              local.get 1
                              local.get 5
                              i32.store offset=8
                            end
                            local.get 0
                            i32.const 8
                            i32.add
                            local.set 0
                            i32.const 18297200
                            local.get 2
                            i32.store
                            i32.const 18297188
                            local.get 4
                            i32.store
                            br 11 (;@1;)
                          end
                          i32.const 18297184
                          i32.load
                          local.tee 11
                          i32.eqz
                          br_if 1 (;@10;)
                          local.get 11
                          i32.ctz
                          i32.const 2
                          i32.shl
                          i32.load offset=18297484
                          local.tee 3
                          i32.load offset=4
                          i32.const -8
                          i32.and
                          local.get 4
                          i32.sub
                          local.set 1
                          local.get 3
                          local.set 2
                          loop  ;; label = @12
                            block  ;; label = @13
                              local.get 3
                              i32.load offset=16
                              local.tee 0
                              i32.eqz
                              if  ;; label = @14
                                local.get 3
                                i32.load offset=20
                                local.tee 0
                                i32.eqz
                                br_if 1 (;@13;)
                              end
                              local.get 0
                              i32.load offset=4
                              i32.const -8
                              i32.and
                              local.get 4
                              i32.sub
                              local.tee 3
                              local.get 1
                              local.get 1
                              local.get 3
                              i32.gt_u
                              local.tee 3
                              select
                              local.set 1
                              local.get 0
                              local.get 2
                              local.get 3
                              select
                              local.set 2
                              local.get 0
                              local.set 3
                              br 1 (;@12;)
                            end
                          end
                          local.get 2
                          i32.load offset=24
                          local.set 9
                          local.get 2
                          local.get 2
                          i32.load offset=12
                          local.tee 0
                          i32.ne
                          if  ;; label = @12
                            local.get 2
                            i32.load offset=8
                            local.tee 3
                            local.get 0
                            i32.store offset=12
                            local.get 0
                            local.get 3
                            i32.store offset=8
                            br 10 (;@2;)
                          end
                          local.get 2
                          i32.load offset=20
                          local.tee 3
                          if (result i32)  ;; label = @12
                            local.get 2
                            i32.const 20
                            i32.add
                          else
                            local.get 2
                            i32.load offset=16
                            local.tee 3
                            i32.eqz
                            br_if 3 (;@9;)
                            local.get 2
                            i32.const 16
                            i32.add
                          end
                          local.set 5
                          loop  ;; label = @12
                            local.get 5
                            local.set 7
                            local.get 3
                            local.tee 0
                            i32.const 20
                            i32.add
                            local.set 5
                            local.get 0
                            i32.load offset=20
                            local.tee 3
                            br_if 0 (;@12;)
                            local.get 0
                            i32.const 16
                            i32.add
                            local.set 5
                            local.get 0
                            i32.load offset=16
                            local.tee 3
                            br_if 0 (;@12;)
                          end
                          local.get 7
                          i32.const 0
                          i32.store
                          br 9 (;@2;)
                        end
                        i32.const -1
                        local.set 4
                        local.get 0
                        i32.const -65
                        i32.gt_u
                        br_if 0 (;@10;)
                        local.get 0
                        i32.const 11
                        i32.add
                        local.tee 1
                        i32.const -8
                        i32.and
                        local.set 4
                        i32.const 18297184
                        i32.load
                        local.tee 9
                        i32.eqz
                        br_if 0 (;@10;)
                        i32.const 31
                        local.set 8
                        local.get 0
                        i32.const 16777204
                        i32.le_u
                        if  ;; label = @11
                          local.get 4
                          i32.const 38
                          local.get 1
                          i32.const 8
                          i32.shr_u
                          i32.clz
                          local.tee 0
                          i32.sub
                          i32.shr_u
                          i32.const 1
                          i32.and
                          local.get 0
                          i32.const 1
                          i32.shl
                          i32.sub
                          i32.const 62
                          i32.add
                          local.set 8
                        end
                        i32.const 0
                        local.get 4
                        i32.sub
                        local.set 1
                        block  ;; label = @11
                          block  ;; label = @12
                            block  ;; label = @13
                              local.get 8
                              i32.const 2
                              i32.shl
                              i32.load offset=18297484
                              local.tee 3
                              i32.eqz
                              if  ;; label = @14
                                i32.const 0
                                local.set 0
                                br 1 (;@13;)
                              end
                              i32.const 0
                              local.set 0
                              local.get 4
                              i32.const 25
                              local.get 8
                              i32.const 1
                              i32.shr_u
                              i32.sub
                              i32.const 0
                              local.get 8
                              i32.const 31
                              i32.ne
                              select
                              i32.shl
                              local.set 2
                              loop  ;; label = @14
                                block  ;; label = @15
                                  local.get 3
                                  i32.load offset=4
                                  i32.const -8
                                  i32.and
                                  local.get 4
                                  i32.sub
                                  local.tee 6
                                  local.get 1
                                  i32.ge_u
                                  br_if 0 (;@15;)
                                  local.get 3
                                  local.set 5
                                  local.get 6
                                  local.tee 1
                                  br_if 0 (;@15;)
                                  i32.const 0
                                  local.set 1
                                  local.get 5
                                  local.set 0
                                  br 3 (;@12;)
                                end
                                local.get 0
                                local.get 3
                                i32.load offset=20
                                local.tee 6
                                local.get 6
                                local.get 3
                                local.get 2
                                i32.const 29
                                i32.shr_u
                                i32.const 4
                                i32.and
                                i32.add
                                i32.load offset=16
                                local.tee 7
                                i32.eq
                                select
                                local.get 0
                                local.get 6
                                select
                                local.set 0
                                local.get 2
                                i32.const 1
                                i32.shl
                                local.set 2
                                local.get 7
                                local.tee 3
                                br_if 0 (;@14;)
                              end
                            end
                            local.get 0
                            local.get 5
                            i32.or
                            i32.eqz
                            if  ;; label = @13
                              i32.const 0
                              local.set 5
                              i32.const 2
                              local.get 8
                              i32.shl
                              local.tee 0
                              i32.const 0
                              local.get 0
                              i32.sub
                              i32.or
                              local.get 9
                              i32.and
                              local.tee 0
                              i32.eqz
                              br_if 3 (;@10;)
                              local.get 0
                              i32.ctz
                              i32.const 2
                              i32.shl
                              i32.load offset=18297484
                              local.set 0
                            end
                            local.get 0
                            i32.eqz
                            br_if 1 (;@11;)
                          end
                          loop  ;; label = @12
                            local.get 0
                            i32.load offset=4
                            i32.const -8
                            i32.and
                            local.get 4
                            i32.sub
                            local.tee 6
                            local.get 1
                            i32.lt_u
                            local.set 2
                            local.get 6
                            local.get 1
                            local.get 2
                            select
                            local.set 1
                            local.get 0
                            local.get 5
                            local.get 2
                            select
                            local.set 5
                            local.get 0
                            i32.load offset=16
                            local.tee 3
                            if (result i32)  ;; label = @13
                              local.get 3
                            else
                              local.get 0
                              i32.load offset=20
                            end
                            local.tee 0
                            br_if 0 (;@12;)
                          end
                        end
                        local.get 5
                        i32.eqz
                        br_if 0 (;@10;)
                        local.get 1
                        i32.const 18297188
                        i32.load
                        local.get 4
                        i32.sub
                        i32.ge_u
                        br_if 0 (;@10;)
                        local.get 5
                        i32.load offset=24
                        local.set 7
                        local.get 5
                        local.get 5
                        i32.load offset=12
                        local.tee 0
                        i32.ne
                        if  ;; label = @11
                          local.get 5
                          i32.load offset=8
                          local.tee 3
                          local.get 0
                          i32.store offset=12
                          local.get 0
                          local.get 3
                          i32.store offset=8
                          br 8 (;@3;)
                        end
                        local.get 5
                        i32.load offset=20
                        local.tee 3
                        if (result i32)  ;; label = @11
                          local.get 5
                          i32.const 20
                          i32.add
                        else
                          local.get 5
                          i32.load offset=16
                          local.tee 3
                          i32.eqz
                          br_if 3 (;@8;)
                          local.get 5
                          i32.const 16
                          i32.add
                        end
                        local.set 2
                        loop  ;; label = @11
                          local.get 2
                          local.set 6
                          local.get 3
                          local.tee 0
                          i32.const 20
                          i32.add
                          local.set 2
                          local.get 0
                          i32.load offset=20
                          local.tee 3
                          br_if 0 (;@11;)
                          local.get 0
                          i32.const 16
                          i32.add
                          local.set 2
                          local.get 0
                          i32.load offset=16
                          local.tee 3
                          br_if 0 (;@11;)
                        end
                        local.get 6
                        i32.const 0
                        i32.store
                        br 7 (;@3;)
                      end
                      local.get 4
                      i32.const 18297188
                      i32.load
                      local.tee 0
                      i32.le_u
                      if  ;; label = @10
                        i32.const 18297200
                        i32.load
                        local.set 1
                        block  ;; label = @11
                          local.get 0
                          local.get 4
                          i32.sub
                          local.tee 3
                          i32.const 16
                          i32.ge_u
                          if  ;; label = @12
                            local.get 1
                            local.get 4
                            i32.add
                            local.tee 2
                            local.get 3
                            i32.const 1
                            i32.or
                            i32.store offset=4
                            local.get 0
                            local.get 1
                            i32.add
                            local.get 3
                            i32.store
                            local.get 1
                            local.get 4
                            i32.const 3
                            i32.or
                            i32.store offset=4
                            br 1 (;@11;)
                          end
                          local.get 1
                          local.get 0
                          i32.const 3
                          i32.or
                          i32.store offset=4
                          local.get 0
                          local.get 1
                          i32.add
                          local.tee 0
                          local.get 0
                          i32.load offset=4
                          i32.const 1
                          i32.or
                          i32.store offset=4
                          i32.const 0
                          local.set 3
                          i32.const 0
                          local.set 2
                        end
                        i32.const 18297188
                        local.get 3
                        i32.store
                        i32.const 18297200
                        local.get 2
                        i32.store
                        local.get 1
                        i32.const 8
                        i32.add
                        local.set 0
                        br 9 (;@1;)
                      end
                      local.get 4
                      i32.const 18297192
                      i32.load
                      local.tee 2
                      i32.lt_u
                      if  ;; label = @10
                        i32.const 18297192
                        local.get 2
                        local.get 4
                        i32.sub
                        local.tee 1
                        i32.store
                        i32.const 18297204
                        i32.const 18297204
                        i32.load
                        local.tee 0
                        local.get 4
                        i32.add
                        local.tee 3
                        i32.store
                        local.get 3
                        local.get 1
                        i32.const 1
                        i32.or
                        i32.store offset=4
                        local.get 0
                        local.get 4
                        i32.const 3
                        i32.or
                        i32.store offset=4
                        local.get 0
                        i32.const 8
                        i32.add
                        local.set 0
                        br 9 (;@1;)
                      end
                      i32.const 0
                      local.set 0
                      local.get 4
                      i32.const 47
                      i32.add
                      local.tee 8
                      block (result i32)  ;; label = @10
                        i32.const 18297652
                        i32.load
                        if  ;; label = @11
                          i32.const 18297660
                          i32.load
                          br 1 (;@10;)
                        end
                        i32.const 18297664
                        i64.const -1
                        i64.store align=4
                        i32.const 18297656
                        i64.const 17592186048512
                        i64.store align=4
                        i32.const 18297652
                        local.get 10
                        i32.const 12
                        i32.add
                        i32.const -16
                        i32.and
                        i32.const 1431655768
                        i32.xor
                        i32.store
                        i32.const 18297672
                        i32.const 0
                        i32.store
                        i32.const 18297624
                        i32.const 0
                        i32.store
                        i32.const 4096
                      end
                      local.tee 1
                      i32.add
                      local.tee 6
                      i32.const 0
                      local.get 1
                      i32.sub
                      local.tee 7
                      i32.and
                      local.tee 5
                      local.get 4
                      i32.le_u
                      br_if 8 (;@1;)
                      i32.const 18297620
                      i32.load
                      local.tee 1
                      if  ;; label = @10
                        i32.const 18297612
                        i32.load
                        local.tee 3
                        local.get 5
                        i32.add
                        local.tee 9
                        local.get 3
                        i32.le_u
                        br_if 9 (;@1;)
                        local.get 1
                        local.get 9
                        i32.lt_u
                        br_if 9 (;@1;)
                      end
                      block  ;; label = @10
                        i32.const 18297624
                        i32.load8_u
                        i32.const 4
                        i32.and
                        i32.eqz
                        if  ;; label = @11
                          block  ;; label = @12
                            block  ;; label = @13
                              block  ;; label = @14
                                block  ;; label = @15
                                  i32.const 18297204
                                  i32.load
                                  local.tee 1
                                  if  ;; label = @16
                                    i32.const 18297628
                                    local.set 0
                                    loop  ;; label = @17
                                      local.get 0
                                      i32.load
                                      local.tee 3
                                      local.get 1
                                      i32.le_u
                                      if  ;; label = @18
                                        local.get 1
                                        local.get 3
                                        local.get 0
                                        i32.load offset=4
                                        i32.add
                                        i32.lt_u
                                        br_if 3 (;@15;)
                                      end
                                      local.get 0
                                      i32.load offset=8
                                      local.tee 0
                                      br_if 0 (;@17;)
                                    end
                                  end
                                  i32.const 0
                                  call 22246
                                  local.tee 2
                                  i32.const -1
                                  i32.eq
                                  br_if 3 (;@12;)
                                  local.get 5
                                  local.set 6
                                  i32.const 18297656
                                  i32.load
                                  local.tee 0
                                  i32.const 1
                                  i32.sub
                                  local.tee 1
                                  local.get 2
                                  i32.and
                                  if  ;; label = @16
                                    local.get 5
                                    local.get 2
                                    i32.sub
                                    local.get 1
                                    local.get 2
                                    i32.add
                                    i32.const 0
                                    local.get 0
                                    i32.sub
                                    i32.and
                                    i32.add
                                    local.set 6
                                  end
                                  local.get 4
                                  local.get 6
                                  i32.ge_u
                                  br_if 3 (;@12;)
                                  i32.const 18297620
                                  i32.load
                                  local.tee 0
                                  if  ;; label = @16
                                    i32.const 18297612
                                    i32.load
                                    local.tee 1
                                    local.get 6
                                    i32.add
                                    local.tee 3
                                    local.get 1
                                    i32.le_u
                                    br_if 4 (;@12;)
                                    local.get 0
                                    local.get 3
                                    i32.lt_u
                                    br_if 4 (;@12;)
                                  end
                                  local.get 6
                                  call 22246
                                  local.tee 0
                                  local.get 2
                                  i32.ne
                                  br_if 1 (;@14;)
                                  br 5 (;@10;)
                                end
                                local.get 6
                                local.get 2
                                i32.sub
                                local.get 7
                                i32.and
                                local.tee 6
                                call 22246
                                local.tee 2
                                local.get 0
                                i32.load
                                local.get 0
                                i32.load offset=4
                                i32.add
                                i32.eq
                                br_if 1 (;@13;)
                                local.get 2
                                local.set 0
                              end
                              local.get 0
                              i32.const -1
                              i32.eq
                              br_if 1 (;@12;)
                              local.get 4
                              i32.const 48
                              i32.add
                              local.get 6
                              i32.le_u
                              if  ;; label = @14
                                local.get 0
                                local.set 2
                                br 4 (;@10;)
                              end
                              i32.const 18297660
                              i32.load
                              local.tee 1
                              local.get 8
                              local.get 6
                              i32.sub
                              i32.add
                              i32.const 0
                              local.get 1
                              i32.sub
                              i32.and
                              local.tee 1
                              call 22246
                              i32.const -1
                              i32.eq
                              br_if 1 (;@12;)
                              local.get 1
                              local.get 6
                              i32.add
                              local.set 6
                              local.get 0
                              local.set 2
                              br 3 (;@10;)
                            end
                            local.get 2
                            i32.const -1
                            i32.ne
                            br_if 2 (;@10;)
                          end
                          i32.const 18297624
                          i32.const 18297624
                          i32.load
                          i32.const 4
                          i32.or
                          i32.store
                        end
                        local.get 5
                        call 22246
                        local.set 2
                        i32.const 0
                        call 22246
                        local.set 0
                        local.get 2
                        i32.const -1
                        i32.eq
                        br_if 5 (;@5;)
                        local.get 0
                        i32.const -1
                        i32.eq
                        br_if 5 (;@5;)
                        local.get 0
                        local.get 2
                        i32.le_u
                        br_if 5 (;@5;)
                        local.get 0
                        local.get 2
                        i32.sub
                        local.tee 6
                        local.get 4
                        i32.const 40
                        i32.add
                        i32.le_u
                        br_if 5 (;@5;)
                      end
                      i32.const 18297612
                      i32.const 18297612
                      i32.load
                      local.get 6
                      i32.add
                      local.tee 0
                      i32.store
                      i32.const 18297616
                      i32.load
                      local.get 0
                      i32.lt_u
                      if  ;; label = @10
                        i32.const 18297616
                        local.get 0
                        i32.store
                      end
                      block  ;; label = @10
                        i32.const 18297204
                        i32.load
                        local.tee 1
                        if  ;; label = @11
                          i32.const 18297628
                          local.set 0
                          loop  ;; label = @12
                            local.get 2
                            local.get 0
                            i32.load
                            local.tee 3
                            local.get 0
                            i32.load offset=4
                            local.tee 5
                            i32.add
                            i32.eq
                            br_if 2 (;@10;)
                            local.get 0
                            i32.load offset=8
                            local.tee 0
                            br_if 0 (;@12;)
                          end
                          br 4 (;@7;)
                        end
                        i32.const 18297196
                        i32.load
                        local.tee 0
                        i32.const 0
                        local.get 0
                        local.get 2
                        i32.le_u
                        select
                        i32.eqz
                        if  ;; label = @11
                          i32.const 18297196
                          local.get 2
                          i32.store
                        end
                        i32.const 0
                        local.set 0
                        i32.const 18297632
                        local.get 6
                        i32.store
                        i32.const 18297628
                        local.get 2
                        i32.store
                        i32.const 18297212
                        i32.const -1
                        i32.store
                        i32.const 18297216
                        i32.const 18297652
                        i32.load
                        i32.store
                        i32.const 18297640
                        i32.const 0
                        i32.store
                        loop  ;; label = @11
                          local.get 0
                          i32.const 3
                          i32.shl
                          local.tee 1
                          local.get 1
                          i32.const 18297220
                          i32.add
                          local.tee 3
                          i32.store offset=18297228
                          local.get 1
                          local.get 3
                          i32.store offset=18297232
                          local.get 0
                          i32.const 1
                          i32.add
                          local.tee 0
                          i32.const 32
                          i32.ne
                          br_if 0 (;@11;)
                        end
                        i32.const 18297192
                        local.get 6
                        i32.const 40
                        i32.sub
                        local.tee 0
                        i32.const -8
                        local.get 2
                        i32.sub
                        i32.const 7
                        i32.and
                        local.tee 1
                        i32.sub
                        local.tee 3
                        i32.store
                        i32.const 18297204
                        local.get 1
                        local.get 2
                        i32.add
                        local.tee 1
                        i32.store
                        local.get 1
                        local.get 3
                        i32.const 1
                        i32.or
                        i32.store offset=4
                        local.get 0
                        local.get 2
                        i32.add
                        i32.const 40
                        i32.store offset=4
                        i32.const 18297208
                        i32.const 18297668
                        i32.load
                        i32.store
                        br 4 (;@6;)
                      end
                      local.get 1
                      local.get 2
                      i32.ge_u
                      br_if 2 (;@7;)
                      local.get 1
                      local.get 3
                      i32.lt_u
                      br_if 2 (;@7;)
                      local.get 0
                      i32.load offset=12
                      i32.const 8
                      i32.and
                      br_if 2 (;@7;)
                      local.get 0
                      local.get 5
                      local.get 6
                      i32.add
                      i32.store offset=4
                      i32.const 18297204
                      local.get 1
                      i32.const -8
                      local.get 1
                      i32.sub
                      i32.const 7
                      i32.and
                      local.tee 0
                      i32.add
                      local.tee 3
                      i32.store
                      i32.const 18297192
                      i32.const 18297192
                      i32.load
                      local.get 6
                      i32.add
                      local.tee 2
                      local.get 0
                      i32.sub
                      local.tee 0
                      i32.store
                      local.get 3
                      local.get 0
                      i32.const 1
                      i32.or
                      i32.store offset=4
                      local.get 1
                      local.get 2
                      i32.add
                      i32.const 40
                      i32.store offset=4
                      i32.const 18297208
                      i32.const 18297668
                      i32.load
                      i32.store
                      br 3 (;@6;)
                    end
                    i32.const 0
                    local.set 0
                    br 6 (;@2;)
                  end
                  i32.const 0
                  local.set 0
                  br 4 (;@3;)
                end
                i32.const 18297196
                i32.load
                local.get 2
                i32.gt_u
                if  ;; label = @7
                  i32.const 18297196
                  local.get 2
                  i32.store
                end
                local.get 2
                local.get 6
                i32.add
                local.set 3
                i32.const 18297628
                local.set 0
                block  ;; label = @7
                  loop  ;; label = @8
                    local.get 3
                    local.get 0
                    i32.load
                    local.tee 5
                    i32.ne
                    if  ;; label = @9
                      local.get 0
                      i32.load offset=8
                      local.tee 0
                      br_if 1 (;@8;)
                      br 2 (;@7;)
                    end
                  end
                  local.get 0
                  i32.load8_u offset=12
                  i32.const 8
                  i32.and
                  i32.eqz
                  br_if 3 (;@4;)
                end
                i32.const 18297628
                local.set 0
                loop  ;; label = @7
                  block  ;; label = @8
                    local.get 0
                    i32.load
                    local.tee 3
                    local.get 1
                    i32.le_u
                    if  ;; label = @9
                      local.get 1
                      local.get 3
                      local.get 0
                      i32.load offset=4
                      i32.add
                      local.tee 3
                      i32.lt_u
                      br_if 1 (;@8;)
                    end
                    local.get 0
                    i32.load offset=8
                    local.set 0
                    br 1 (;@7;)
                  end
                end
                i32.const 18297192
                local.get 6
                i32.const 40
                i32.sub
                local.tee 0
                i32.const -8
                local.get 2
                i32.sub
                i32.const 7
                i32.and
                local.tee 5
                i32.sub
                local.tee 7
                i32.store
                i32.const 18297204
                local.get 2
                local.get 5
                i32.add
                local.tee 5
                i32.store
                local.get 5
                local.get 7
                i32.const 1
                i32.or
                i32.store offset=4
                local.get 0
                local.get 2
                i32.add
                i32.const 40
                i32.store offset=4
                i32.const 18297208
                i32.const 18297668
                i32.load
                i32.store
                local.get 1
                local.get 3
                i32.const 39
                local.get 3
                i32.sub
                i32.const 7
                i32.and
                i32.add
                i32.const 47
                i32.sub
                local.tee 0
                local.get 0
                local.get 1
                i32.const 16
                i32.add
                i32.lt_u
                select
                local.tee 5
                i32.const 27
                i32.store offset=4
                local.get 5
;; Exports: free
  (func (;22239;) (type 0) (param i32)
    (local i32 i32 i32 i32 i32 i32 i32 i32)
    block  ;; label = @1
      local.get 0
      i32.eqz
      br_if 0 (;@1;)
      local.get 0
      i32.const 8
      i32.sub
      local.tee 3
      local.get 0
      i32.const 4
      i32.sub
      i32.load
      local.tee 1
      i32.const -8
      i32.and
      local.tee 0
      i32.add
      local.set 4
      block  ;; label = @2
        local.get 1
        i32.const 1
        i32.and
        br_if 0 (;@2;)
        local.get 1
        i32.const 2
        i32.and
        i32.eqz
        br_if 1 (;@1;)
        local.get 3
        local.get 3
        i32.load
        local.tee 2
        i32.sub
        local.tee 3
        i32.const 18297196
        i32.load
        i32.lt_u
        br_if 1 (;@1;)
        local.get 0
        local.get 2
        i32.add
        local.set 0
        block  ;; label = @3
          block  ;; label = @4
            block  ;; label = @5
              i32.const 18297200
              i32.load
              local.get 3
              i32.ne
              if  ;; label = @6
                local.get 3
                i32.load offset=12
                local.set 1
                local.get 2
                i32.const 255
                i32.le_u
                if  ;; label = @7
                  local.get 1
                  local.get 3
                  i32.load offset=8
                  local.tee 5
                  i32.ne
                  br_if 2 (;@5;)
                  i32.const 18297180
                  i32.const 18297180
                  i32.load
                  i32.const -2
                  local.get 2
                  i32.const 3
                  i32.shr_u
                  i32.rotl
                  i32.and
                  i32.store
                  br 5 (;@2;)
                end
                local.get 3
                i32.load offset=24
                local.set 6
                local.get 1
                local.get 3
                i32.ne
                if  ;; label = @7
                  local.get 3
                  i32.load offset=8
                  local.tee 2
                  local.get 1
                  i32.store offset=12
                  local.get 1
                  local.get 2
                  i32.store offset=8
                  br 4 (;@3;)
                end
                local.get 3
                i32.load offset=20
                local.tee 2
                if (result i32)  ;; label = @7
                  local.get 3
                  i32.const 20
                  i32.add
                else
                  local.get 3
                  i32.load offset=16
                  local.tee 2
                  i32.eqz
                  br_if 3 (;@4;)
                  local.get 3
                  i32.const 16
                  i32.add
                end
                local.set 5
                loop  ;; label = @7
                  local.get 5
                  local.set 8
                  local.get 2
                  local.tee 1
                  i32.const 20
                  i32.add
                  local.set 5
                  local.get 1
                  i32.load offset=20
                  local.tee 2
                  br_if 0 (;@7;)
                  local.get 1
                  i32.const 16
                  i32.add
                  local.set 5
                  local.get 1
                  i32.load offset=16
                  local.tee 2
                  br_if 0 (;@7;)
                end
                local.get 8
                i32.const 0
                i32.store
                br 3 (;@3;)
              end
              local.get 4
              i32.load offset=4
              local.tee 1
              i32.const 3
              i32.and
              i32.const 3
              i32.ne
              br_if 3 (;@2;)
              i32.const 18297188
              local.get 0
              i32.store
              local.get 4
              local.get 1
              i32.const -2
              i32.and
              i32.store offset=4
              local.get 3
              local.get 0
              i32.const 1
              i32.or
              i32.store offset=4
              local.get 4
              local.get 0
              i32.store
              return
            end
            local.get 5
            local.get 1
            i32.store offset=12
            local.get 1
            local.get 5
            i32.store offset=8
            br 2 (;@2;)
          end
          i32.const 0
          local.set 1
        end
        local.get 6
        i32.eqz
        br_if 0 (;@2;)
        block  ;; label = @3
          local.get 3
          i32.load offset=28
          local.tee 5
          i32.const 2
          i32.shl
          local.tee 2
          i32.load offset=18297484
          local.get 3
          i32.eq
          if  ;; label = @4
            local.get 2
            i32.const 18297484
            i32.add
            local.get 1
            i32.store
            local.get 1
            br_if 1 (;@3;)
            i32.const 18297184
            i32.const 18297184
            i32.load
            i32.const -2
            local.get 5
            i32.rotl
            i32.and
            i32.store
            br 2 (;@2;)
          end
          block  ;; label = @4
            local.get 3
            local.get 6
            i32.load offset=16
            i32.eq
            if  ;; label = @5
              local.get 6
              local.get 1
              i32.store offset=16
              br 1 (;@4;)
            end
            local.get 6
            local.get 1
            i32.store offset=20
          end
          local.get 1
          i32.eqz
          br_if 1 (;@2;)
        end
        local.get 1
        local.get 6
        i32.store offset=24
        local.get 3
        i32.load offset=16
        local.tee 2
        if  ;; label = @3
          local.get 1
          local.get 2
          i32.store offset=16
          local.get 2
          local.get 1
          i32.store offset=24
        end
        local.get 3
        i32.load offset=20
        local.tee 2
        i32.eqz
        br_if 0 (;@2;)
        local.get 1
        local.get 2
        i32.store offset=20
        local.get 2
        local.get 1
        i32.store offset=24
      end
      local.get 3
      local.get 4
      i32.ge_u
      br_if 0 (;@1;)
      local.get 4
      i32.load offset=4
      local.tee 2
      i32.const 1
      i32.and
      i32.eqz
      br_if 0 (;@1;)
      block  ;; label = @2
        block  ;; label = @3
          block  ;; label = @4
            block  ;; label = @5
              local.get 2
              i32.const 2
              i32.and
              i32.eqz
              if  ;; label = @6
                i32.const 18297204
                i32.load
                local.get 4
                i32.eq
                if  ;; label = @7
                  i32.const 18297204
                  local.get 3
                  i32.store
                  i32.const 18297192
                  i32.const 18297192
                  i32.load
                  local.get 0
                  i32.add
                  local.tee 0
                  i32.store
                  local.get 3
                  local.get 0
                  i32.const 1
                  i32.or
                  i32.store offset=4
                  local.get 3
                  i32.const 18297200
                  i32.load
                  i32.ne
                  br_if 6 (;@1;)
                  i32.const 18297188
                  i32.const 0
                  i32.store
                  i32.const 18297200
                  i32.const 0
                  i32.store
                  return
                end
                i32.const 18297200
                i32.load
                local.tee 6
                local.get 4
                i32.eq
                if  ;; label = @7
                  i32.const 18297200
                  local.get 3
                  i32.store
                  i32.const 18297188
                  i32.const 18297188
                  i32.load
                  local.get 0
                  i32.add
                  local.tee 0
                  i32.store
                  local.get 3
                  local.get 0
                  i32.const 1
                  i32.or
                  i32.store offset=4
                  local.get 0
                  local.get 3
                  i32.add
                  local.get 0
                  i32.store
                  return
                end
                local.get 2
                i32.const -8
                i32.and
                local.get 0
                i32.add
                local.set 0
                local.get 4
                i32.load offset=12
                local.set 1
                local.get 2
                i32.const 255
                i32.le_u
                if  ;; label = @7
                  local.get 4
                  i32.load offset=8
                  local.tee 5
                  local.get 1
                  i32.eq
                  if  ;; label = @8
                    i32.const 18297180
                    i32.const 18297180
                    i32.load
                    i32.const -2
                    local.get 2
                    i32.const 3
                    i32.shr_u
                    i32.rotl
                    i32.and
                    i32.store
                    br 5 (;@3;)
                  end
                  local.get 5
                  local.get 1
                  i32.store offset=12
                  local.get 1
                  local.get 5
                  i32.store offset=8
                  br 4 (;@3;)
                end
                local.get 4
                i32.load offset=24
                local.set 7
                local.get 1
                local.get 4
                i32.ne
                if  ;; label = @7
                  local.get 4
                  i32.load offset=8
                  local.tee 2
                  local.get 1
                  i32.store offset=12
                  local.get 1
                  local.get 2
                  i32.store offset=8
                  br 3 (;@4;)
                end
                local.get 4
                i32.load offset=20
                local.tee 2
                if (result i32)  ;; label = @7
                  local.get 4
                  i32.const 20
                  i32.add
                else
                  local.get 4
                  i32.load offset=16
                  local.tee 2
                  i32.eqz
                  br_if 2 (;@5;)
                  local.get 4
                  i32.const 16
                  i32.add
                end
                local.set 5
                loop  ;; label = @7
                  local.get 5
                  local.set 8
                  local.get 2
                  local.tee 1
                  i32.const 20
                  i32.add
                  local.set 5
                  local.get 1
                  i32.load offset=20
                  local.tee 2
                  br_if 0 (;@7;)
                  local.get 1
                  i32.const 16
                  i32.add
                  local.set 5
                  local.get 1
                  i32.load offset=16
                  local.tee 2
                  br_if 0 (;@7;)
                end
                local.get 8
                i32.const 0
                i32.store
                br 2 (;@4;)
              end
              local.get 4
              local.get 2
              i32.const -2
              i32.and
              i32.store offset=4
              local.get 3
              local.get 0
              i32.const 1
              i32.or
              i32.store offset=4
              local.get 0
              local.get 3
              i32.add
              local.get 0
              i32.store
              br 3 (;@2;)
            end
            i32.const 0
            local.set 1
          end
          local.get 7
          i32.eqz
          br_if 0 (;@3;)
          block  ;; label = @4
            local.get 4
            i32.load offset=28
            local.tee 5
            i32.const 2
            i32.shl
            local.tee 2
            i32.load offset=18297484
            local.get 4
            i32.eq
            if  ;; label = @5
              local.get 2
              i32.const 18297484
              i32.add
              local.get 1
              i32.store
              local.get 1
              br_if 1 (;@4;)
              i32.const 18297184
              i32.const 18297184
              i32.load
              i32.const -2
              local.get 5
              i32.rotl
              i32.and
              i32.store
              br 2 (;@3;)
            end
            block  ;; label = @5
              local.get 4
              local.get 7
              i32.load offset=16
              i32.eq
              if  ;; label = @6
                local.get 7
                local.get 1
                i32.store offset=16
                br 1 (;@5;)
              end
              local.get 7
              local.get 1
              i32.store offset=20
            end
            local.get 1
            i32.eqz
            br_if 1 (;@3;)
          end
          local.get 1
          local.get 7
          i32.store offset=24
          local.get 4
          i32.load offset=16
          local.tee 2
          if  ;; label = @4
            local.get 1
            local.get 2
            i32.store offset=16
            local.get 2
            local.get 1
            i32.store offset=24
          end
          local.get 4
          i32.load offset=20
          local.tee 2
          i32.eqz
          br_if 0 (;@3;)
          local.get 1
          local.get 2
          i32.store offset=20
          local.get 2
          local.get 1
          i32.store offset=24
        end
        local.get 3
        local.get 0
        i32.const 1
        i32.or
        i32.store offset=4
        local.get 0
        local.get 3
        i32.add
        local.get 0
        i32.store
        local.get 3
        local.get 6
        i32.ne
        br_if 0 (;@2;)
        i32.const 18297188
        local.get 0
        i32.store
        return
      end
      local.get 0
      i32.const 255
      i32.le_u
      if  ;; label = @2
        local.get 0
        i32.const 248
        i32.and
        i32.const 18297220
        i32.add
        local.set 1
        block (result i32)  ;; label = @3
          i32.const 18297180
          i32.load
          local.tee 2
          i32.const 1
          local.get 0
          i32.const 3
          i32.shr_u
          i32.shl
          local.tee 0
          i32.and
          i32.eqz
          if  ;; label = @4
            i32.const 18297180
            local.get 0
            local.get 2
            i32.or
            i32.store
            local.get 1
            br 1 (;@3;)
          end
          local.get 1
          i32.load offset=8
        end
        local.set 0
        local.get 1
        local.get 3
        i32.store offset=8
        local.get 0
        local.get 3
        i32.store offset=12
        local.get 3
        local.get 1
        i32.store offset=12
        local.get 3
        local.get 0
        i32.store offset=8
        return
      end
      i32.const 31
      local.set 1
      local.get 0
      i32.const 16777215
      i32.le_u
      if  ;; label = @2
        local.get 0
        i32.const 38
        local.get 0
        i32.const 8
        i32.shr_u
        i32.clz
        local.tee 1
        i32.sub
        i32.shr_u
        i32.const 1
        i32.and
        local.get 1
        i32.const 1
        i32.shl
        i32.or
        i32.const 62
        i32.xor
        local.set 1
      end
      local.get 3
      local.get 1
      i32.store offset=28
      local.get 3
      i64.const 0
      i64.store offset=16 align=4
      local.get 1
      i32.const 2
      i32.shl
      i32.const 18297484
      i32.add
      local.set 5
      block (result i32)  ;; label = @2
        block  ;; label = @3
          block (result i32)  ;; label = @4
            i32.const 18297184
            i32.load
            local.tee 2
            i32.const 1
            local.get 1
            i32.shl
            local.tee 4
            i32.and
            i32.eqz
            if  ;; label = @5
              i32.const 18297184
              local.get 2
              local.get 4
              i32.or
              i32.store
              local.get 5
              local.get 3
              i32.store
              i32.const 24
              local.set 1
              i32.const 8
              br 1 (;@4;)
            end
            local.get 0
            i32.const 25
            local.get 1
            i32.const 1
            i32.shr_u
            i32.sub
            i32.const 0
            local.get 1
            i32.const 31
            i32.ne
            select
            i32.shl
            local.set 1
            local.get 5
            i32.load
            local.set 5
            loop  ;; label = @5
              local.get 5
              local.tee 2
              i32.load offset=4
              i32.const -8
              i32.and
              local.get 0
              i32.eq
              br_if 2 (;@3;)
              local.get 1
              i32.const 29
              i32.shr_u
              local.set 5
              local.get 1
              i32.const 1
              i32.shl
              local.set 1
              local.get 2
              local.get 5
              i32.const 4
              i32.and
              i32.add
              local.tee 4
              i32.load offset=16
              local.tee 5
              br_if 0 (;@5;)
            end
            local.get 4
            local.get 3
            i32.store offset=16
            i32.const 24
            local.set 1
            local.get 2
            local.set 5
            i32.const 8
          end
          local.set 0
          local.get 3
          local.set 2
          local.get 3
          br 1 (;@2;)
        end
        local.get 2
        i32.load offset=8
        local.tee 5
        local.get 3
        i32.store offset=12
        local.get 2
        local.get 3
        i32.store offset=8
        i32.const 24
        local.set 0
        i32.const 8
        local.set 1
        i32.const 0
      end
      local.set 4
      local.get 1
      local.get 3
      i32.add
      local.get 5
      i32.store
      local.get 3
      local.get 2
      i32.store offset=12
      local.get 0
      local.get 3
      i32.add
      local.get 4
      i32.store
      i32.const 18297212
      i32.const 18297212
      i32.load
      i32.const 1
      i32.sub
      local.tee 3
      i32.const -1
      local.get 3
      select
      i32.store
    end)
